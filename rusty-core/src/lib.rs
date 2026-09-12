use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod rusty_core {
    use pyo3::prelude::*;
    use rusqlite::Connection;

    #[pyfunction]
    fn init_db() {
        let db_conn = Connection::open("test.db").unwrap();

        db_conn.execute("
            CREATE TABLE IF NOT EXISTS modrole (
                guild_id INTEGER PRIMARY KEY NOT NULL
                role_ids INTERGER
            )
        ", []).unwrap(); // Not permament will be changed in the soon...
    }

    #[pyfunction]
    fn test_fn() {
        println!("The snake has been oxidised")
    }
}
