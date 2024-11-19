import os 
import base64
from time import time
from argparse import ArgumentParser

from lzw import encode
from lzw import decode

def binary_string_to_bytes(binary_string):
    # Ensure the length of the binary string is a multiple of 8
    if len(binary_string) % 8 != 0:
        # Pad the binary string to make it a multiple of 8 bits
        binary_string = binary_string.ljust(len(binary_string) + (8 - len(binary_string) % 8), '0')

    # Convert the binary string to bytes
    byte_data = bytearray()
    for i in range(0, len(binary_string), 8):
        byte_data.append(int(binary_string[i:i+8], 2))
    return byte_data

def bytes_to_binary_string(byte_data):
    binary_string = ''.join(format(byte, '08b') for byte in byte_data)
    return binary_string

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
group.add_argument (
    '-x', '--x',
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

    lz_extension:str = '.lzw' # default extension to output compression
    txt_extension:str = '.txt' # default extension to output descompression
    descompression_token:str = '__dec' # token to descompression

    args = parser.parse_args()

    print('\nLZW Compression and Decompression')
    print('| Settings: ')
    print('| - Number of Bits: {}'.format(args.n))
    print('| - Fixed Bits Size: {}'.format(args.f))
    print('| - To Compress File: {}'.format(args.c))
    print('| - To Descompress File Descompression: {}'.format(args.d))
    

    if args.c: 

        # Compression Case
        output_file:str = ''
        if args.o:
            # Using output file path when it is parsed.
            output_file = args.o
        else:
            dot_position:int = args.c[::-1].find('.')
            if dot_position > -1:
                output_file= args.c[:-(dot_position+1)]+ lz_extension
            else:
                output_file= args.c+ lz_extension
        
        print('| - Output File: {}'.format(output_file))
        print('\n\nCompressing...')

        start_timer = time()
        content:str = None
        with open(args.c, 'rb') as f:
            content = base64.b64encode(f.read()).decode('ascii')
        
        # print(content)
        encode_text = encode(texto=content, params_bits=args.n, is_fixed=args.f)
        binary_data = binary_string_to_bytes(encode_text)
        # Write binary data to a file
        # print(binary_data)
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
        # Descompression Case
        output_file:str = ''
        if args.o:
            # Using output file path when it is parsed.
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

        binary_string_read = bytes_to_binary_string(content)
        decode_text = decode(text_encoded=binary_string_read, params_bits=args.n, is_fixed=args.f)
        with open(output_file, "wb") as file:
            file.write(base64.b64decode(decode_text))
