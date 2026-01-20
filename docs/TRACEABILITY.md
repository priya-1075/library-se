# Traceability Matrix Library Book Management System

Purpose : Map requirements (user stories) to implementation and tests, and show when each was delivered .

| Req ID |                User Story             | Sprint    | Implementation (Code) | Verification (Tests) | Release Tag | Status  |
| US1    | Add a book with ID, title, and author | Sprint -1 | 'src/library.py' -> 'Library.add_book()' | 'tests/test_library.py' -> 
'test_add_book_success', 'test_add_book_duplicate' | v0.1 | Done |
| US2    | Borrow a book from the library        | Sprint -2 | 'src/library.py' -> 'Library.borrow_book()' | 'tests/test_library.py' -> 
'test_borrow_book', 'test_borrow_unavailable_book' | v0.2 | Done |
| US3    | Return a borrowed book                | Sprint -2 | 'src/library.py' -> 'Library.return_book()' | 'tests/test_library.py' -> 
'test_return_book' | v0.2 | Done |
| US4    | Generate library status report        | Sprint -3 | 'src/library.py' -> 'Library.generate_report()' | 'tests/test_library.py' -> 
'test_generate_report_header', 'test_generate_report_contains_book'  | v0.3 | Done |
