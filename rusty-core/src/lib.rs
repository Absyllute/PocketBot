use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod rusty_core {

use pyo3::prelude::*;
    use rusqlite::{Connection, params};

    const DATABASE: &str = "test.db";

    /// init_db creates the database if it doesnt exist.
    #[pyfunction]
    fn init_db() {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS modrole (
                guild_id INTEGER NOT NULL,
                role_id  INTEGER NOT NULL,
                PRIMARY KEY (guild_id, role_id)
            )
        ", []).unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS mc_server (
                guild_id     INTEGER NOT NULL PRIMARY KEY,
                java_link    TEXT NOT NULL,
                bedrock_link TEXT,
                bedrock_port INTEGER,
                embed_title  TEXT NOT NULL,
                embed_desc   TEXT
            )
        ", []).unwrap();
    }

    #[pyfunction]
    fn setup_join_link (guild_id: i64, java_link: &str, bedrock_link: &str, bedrock_port: i64, embed_title: &str, embed_desc: &str) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            INSERT OR REPLACE INTO mc_server (guild_id, java_link, bedrock_link, bedrock_port, embed_title, embed_desc)
        ", params![guild_id, java_link, bedrock_link, bedrock_port, embed_title, embed_desc]).unwrap();
    }

    /// Adds a role id into the modrole group
    #[pyfunction]
    fn add_modrole(guild_id: i64, role_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            INSERT OR IGNORE INTO modrole (guild_id, role_id) VALUES (?1, ?2)
        ", rusqlite::params![guild_id, role_id]).unwrap();
    }

    /// Removes a role id into the modrole group
    #[pyfunction]
    fn remove_modrole(guild_id: i64, role_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            DELETE FROM modrole WHERE guild_id = ?1 AND role_id = ?2
        ", params![guild_id, role_id.to_string()]).unwrap();
    }

    /// Returns an array of i64 role ids
    #[pyfunction]
    fn check_modroles(guild_id: i64) -> PyResult<Vec<i64>> {
        let db_conn = Connection::open(DATABASE).unwrap();

        let mut stmt = db_conn.prepare("SELECT role_id FROM modrole WHERE guild_id = ?1").unwrap();

        let role_iterator = stmt.query_map(params![guild_id], |row| {
            let role_id: i64 = row.get(0)?;
            Ok(role_id)
        }).unwrap();

        let mut roles = Vec::new();
        for role in role_iterator {
            roles.push(role.unwrap());
        }

        Ok(roles)
    }
}
