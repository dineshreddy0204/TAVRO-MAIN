//! MemoryBackend trait for all storage backends.

use tavro_core::{TavroError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, TavroError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, TavroError>;
    fn delete(&self, doc_id: &str) -> Result<bool, TavroError>;
    fn clear(&self) -> Result<(), TavroError>;
    fn count(&self) -> Result<usize, TavroError>;
}
