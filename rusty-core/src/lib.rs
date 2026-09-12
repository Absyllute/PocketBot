use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod rusty_core {
    use pyo3::prelude::*;
    use rusqlite::{Connection};

    const DATABASE: &str = "test.db";

    /// init_db creates the database if it doesnt exist.
    #[pyfunction]
    fn init_db() {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS modrole (
                guild_id INTEGER PRIMARY KEY NOT NULL,
                role_ids TEXT
            )
        ", []).unwrap();

        println!("Rust: Initalised Databse")
    }

    #[pyfunction]
    fn add_modrole(guild_id: i64, role_ids: Vec<i64>) {
        let db_conn = Connection::open(DATABASE).unwrap();

        let json_roles = serde_json::to_string(&role_ids).unwrap();

        db_conn.execute("
            INSERT INTO modrole (guild_id, role_id) VALUES (?1, ?2)
            ON CONFLICT (guild_id) DO UPDATE SET role_ids = excluded.role_ids
        ", rusqlite::params![guild_id, json_roles]).unwrap();
    }

    #[pyfunction]
    fn test_fn() {
        println!("The snake has been oxidised")
    }
}
