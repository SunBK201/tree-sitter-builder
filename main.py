from tree_sitter import Language

Language.build_library(
    # Store the library in the `build` directory
    "build/languages.so",
    # Include one or more languages
    [
        "vendor/tree-sitter-cpp",
        "vendor/tree-sitter-java",
        "vendor/tree-sitter-python",
        "vendor/tree-sitter-javascript",
        "vendor/tree-sitter-typescript/typescript",
    ]
)
