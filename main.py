import os 
from time import time
from argparse import ArgumentParser

from lzw import encode
from lzw import decode

parser = ArgumentParser(description='Compression and Decompression LZW (Lempel-Ziv-Welch) algorithm implemented in Python')

group = parser.add_mutually_exclusive_group(required=True)

# argumento pra compressar
group.add_argument (
    '-c', '--c',
    type=str,
    default=None,
    action='store',
    metavar='',
    help='Path to the input file that will be compressed.'
)

# argumento para descompressar
group.add_argument (
    '-d', '--d',
    type=str,
    default=None,
    action='store',
    metavar='',
    help='Path to the input file that will be decompressed'   
)

parser.add_argument (
    '-o', '--o',
    type=str,
    default=None,
    required=False,
    metavar='',
    help='This should be the output file path, but it is optional.'
)

parser.add_argument (
    '-f', '--f',
    default=False,
    action="store_true",
    help='Bits are fixed or not.'
)

parser.add_argument (
    '-n', '--n',
    type=int,
    default=12,
    action='store',
    metavar='',
    help='Bits number.'
)

if __name__ == '__main__': 

    lz_extension:str = '.lzw' # extensao padrao para saida da compressao
    txt_extension:str = '.txt' # extensao padrao para saida da descompressao
    descompression_token:str = '__dec' # token para descompressao

    args = parser.parse_args()

    print('\nLZW Compression and Decompression')
    print('| Settings: ')
    print('| - Number of Bits: {}'.format(args.n))
    print('| - Fixed Bits Size: {}'.format(args.f))
    print('| - To Compress File: {}'.format(args.c))
    print('| - To Descompress File Descompression: {}'.format(args.d))
    

    if args.c: 

        # Caso da compressao
        output_file:str = ''
        if args.o:
            # se eh parsed, usamos o caminho do output file.
            output_file = args.o
        else:
            dot_position:int = args.c[::-1].find('.')
            if dot_position > -1:
                output_file= args.c[:-(dot_position+1)]+ lz_extension
            else:
                output_file= args.c+ lz_extension
        
        print('| - Output File: {}'.format(output_file))
        print('\n\nCompressing...')

        # verificacao do tempo de compressao
        start_timer = time()
        content:str = None
        with open(args.c, 'r', encoding="ascii") as file:
            content = file.read()
        
        encode_text = '1' + encode(texto=content, params_bits=args.n, is_fixed=args.f)

        binary_data = int(encode_text, 2).to_bytes((len(encode_text) + 7) // 8, byteorder="big")

        with open(output_file, "wb") as file:
            file.write(binary_data)
        
        execution_time = time() - start_timer
        print('File Compressed!\n')
        
        original_size = os.path.getsize(args.c)
        compressed_size = os.path.getsize(output_file)
        
        print('| Compression Statistics:')
        print('|- Compressed in {:.5f}s'.format(execution_time))
        print('|- Original File Size: {:.0f} Bytes'.format(original_size))
        print('|- Compressed File Size: {:.0f} Bytes'.format(compressed_size))
        print('|- Compression Ratio: {:.4f}%'.format((compressed_size / original_size) * 100))

    elif args.d:
        # caso de descompressao
        output_file:str = ''
        if args.o:
            # se eh parsed, usamos o caminho do output file.
            output_file = args.o
        else:
            dot_position:int = args.d[::-1].find('.')
            if dot_position > -1:
                output_file= args.d[:-(dot_position+1)]+ descompression_token + txt_extension
            else:
                output_file= args.d + descompression_token + txt_extension

        print('| - Output File: {}'.format(output_file))
        print('\n\nDescompressing...')

        content:str = None
        with open(args.d, 'rb') as file:
            content = file.read()
        
        binary_string_read = bin(int.from_bytes(content, byteorder="big"))[2:].zfill(len(content))
        binary_string_read = binary_string_read[1:]
        decode_text = decode(text_encoded=binary_string_read, params_bits=args.n, is_fixed=args.f)
        with open(output_file, "w") as file:
            file.write(decode_text)
        print('File Descompressed!')