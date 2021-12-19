CFG = {
    # путь к хранилищу документов
    'storage': {
        'dir': './storage',
    },

    # адреса серверов
    'dispatcher_address': 'localhost:50051',
    'storage_address': 'localhost:50052',
    'document_address': 'localhost:0',

    # секретный ключ для проверки доступа к сервису
    'secret_key': '123456',
}