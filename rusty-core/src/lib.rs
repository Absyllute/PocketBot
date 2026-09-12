use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod rusty_core {
    use pyo3::prelude::*;
    use rusqlite::Connection;

    /// init_db creates the database if it doesnt exist.
    #[pyfunction]
    fn init_db() {
        let db_conn = Connection::open("test.db").unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS modrole (
                guild_id INTEGER PRIMARY KEY NOT NULL,
                role_ids TEXT
            )
        ", []).unwrap();
    }

    #[pyfunction]
    fn test_fn() {
        println!("The snake has been oxidised")
    }
}
