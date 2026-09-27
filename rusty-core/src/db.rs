use pyo3::prelude::*;
use crate::DATABASE;
use rusqlite::{Connection};

/// init_db creates the database and tables they dont exist.
    #[pyfunction]
    pub fn init_db() {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS tb_modroles (
                guild_id INTEGER NOT NULL,
                role_id  INTEGER NOT NULL,
                PRIMARY KEY (guild_id, role_id)
            )
        ", []).unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS tb_mcserver (
                guild_id     INTEGER NOT NULL PRIMARY KEY,
                java_link    TEXT,
                bedrock_link TEXT,
                bedrock_port INTEGER,
                embed_title  TEXT NOT NULL,
                embed_desc   TEXT
            )
        ", []).unwrap();
    }