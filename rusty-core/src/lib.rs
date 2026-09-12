use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod rusty_core {
    use pyo3::prelude::*;

    #[pyfunction]
    fn test_fn() {
        println!("The snake has been oxidised")
    }
}
