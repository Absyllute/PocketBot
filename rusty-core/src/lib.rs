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
                guild_id INTEGER PRIMARY KEY NOT NULL,
                role_id  TEXT
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
            ON CONFLICT (guild_id) DO UPDATE SET role_id = excluded.role_id
        ", rusqlite::params![guild_id, json_roles]).unwrap();
    }

    #[pyfunction]
    fn remove_modrole(guild_id: i64, role_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            DELETE FROM modrole WHERE guild_id = ?1 AND role_id = ?2
        ", params![guild_id, role_id.to_string()]).unwrap();
    }

    #[pyfunction]
    fn test_fn() {
        println!("The snake has been oxidised")
    }
}
