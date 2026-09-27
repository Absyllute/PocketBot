use pyo3::prelude::*;
use rusqlite::{Connection, params};
use crate::DATABASE;

/// Sets up the SMP join links for the guild the command is run in.
    #[pyfunction]
    pub fn setup_join_links (guild_id: i64, java_link: &str, bedrock_link: &str, bedrock_port: i64, embed_title: &str, embed_desc: &str) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            INSERT OR REPLACE INTO tb_mcserver (guild_id, java_link, bedrock_link, bedrock_port, embed_title, embed_desc)
            VALUES(?1, ?2, ?3, ?4, ?5, ?6)
        ", params![guild_id, java_link, bedrock_link, bedrock_port, embed_title, embed_desc]).unwrap();
    }

    #[pyfunction]
    pub fn remove_join_links (guild_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute(
            "DELETE FROM tb_mcserver WHERE guild_id = ?1",
            params![guild_id]).unwrap();
    }

    #[pyfunction]
    pub fn check_join_links(guild_id: i64) -> PyResult<Option<(Option<String>, Option<String>, Option<i64>, String, Option<String>)>> {
        let db_conn = Connection::open(DATABASE).unwrap();

        let mut stmt = db_conn.prepare("SELECT java_link, bedrock_link, bedrock_port, embed_title, embed_desc FROM tb_mcserver WHERE guild_id = ?1").unwrap();

        let iter = stmt.query_map(params![guild_id], |row| {
            Ok((
                row.get::<usize, Option<String>>(0)?, // Java link
                row.get::<usize, Option<String>>(1)?, // Bedrock link
                row.get::<usize, Option<i64>>(2)?,    // Bedrock port
                row.get::<usize, String>(3)?,         // Embed title
                row.get::<usize, Option<String>>(4)?  // Embed description
            ))
        }).unwrap();

        let mut result = None;

        for row in iter {
            result = Some(row.unwrap());
        }

        Ok(result)
    }