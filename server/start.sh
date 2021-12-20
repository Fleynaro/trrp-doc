#! /bin/sh
python3 ./start_dispatcher.py &
python3 ./start_storage.py &
python3 ./start_doc_service.py &
python3 ./start_doc_service.py && fg