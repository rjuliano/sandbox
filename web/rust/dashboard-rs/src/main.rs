#![recursion_limit = "1024"]

#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

use console_error_panic_hook::set_once as set_panic_hook;
use myalerts;
use web_sys::window;

fn start_app() {
    let document = window().and_then(|win| win.document()).expect("Could not access document");
    let body = document.body().expect("Could not access document.body");
    let text_node = document.create_text_node("Rust/WASM example.");
    body.append_child(text_node.as_ref()).expect("Failed to append text");
}

fn main() {
    set_panic_hook();
    start_app();
    myalerts::wasm::greet("From the greet function in myalerts crate.")
}