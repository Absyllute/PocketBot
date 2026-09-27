use pyo3::prelude::*;
use rusqlite::{Connection, params};
use crate::DATABASE;

/// Adds a role id into the modrole group
    #[pyfunction]
    pub fn add_modrole(guild_id: i64, role_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            INSERT OR IGNORE INTO tb_modroles (guild_id, role_id) VALUES (?1, ?2)
        ", rusqlite::params![guild_id, role_id]).unwrap();
    }

    /// Removes a role id into the modrole group
    #[pyfunction]
    pub fn remove_modrole(guild_id: i64, role_id: i64) {
        let db_conn = Connection::open(DATABASE).unwrap();

        db_conn.execute("
            DELETE FROM tb_modroles WHERE guild_id = ?1 AND role_id = ?2
        ", params![guild_id, role_id.to_string()]).unwrap();
    }

    /// Checks what roles are part of the ModRoles group.
    /// Retuning an array of i64's
    #[pyfunction]
    pub fn check_modroles(guild_id: i64) -> PyResult<Vec<i64>> {
        let db_conn = Connection::open(DATABASE).unwrap();

        let mut stmt = db_conn.prepare("SELECT role_id FROM tb_modroles WHERE guild_id = ?1").unwrap();

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