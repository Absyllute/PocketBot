mod db;
mod modroles;
mod mc_server;

use pyo3::prelude::*;

pub const DATABASE: &str = "prod.db";


/// A Python module implemented in Rust.
#[pymodule]
fn bot_backend (m: &Bound<'_, PyModule>) -> PyResult<()> {
    
    // --- mc_server.rs --- //
    m.add_function(wrap_pyfunction!(mc_server::check_join_links, m)?)?;
    m.add_function(wrap_pyfunction!(mc_server::setup_join_links, m)?)?;
    m.add_function(wrap_pyfunction!(mc_server::remove_join_links, m)?)?;

    // --- db.rs -- //
    m.add_function(wrap_pyfunction!(db::init_db, m)?)?;

    // --- modroles.rs --- //
    m.add_function(wrap_pyfunction!(modroles::add_modrole, m)?)?;
    m.add_function(wrap_pyfunction!(modroles::check_modroles, m)?)?;
    m.add_function(wrap_pyfunction!(modroles::remove_modrole, m)?)?;

    Ok(())
}
