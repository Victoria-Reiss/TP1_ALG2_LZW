ASCII_chars = [
    "\x00", "\x01", "\x02", "\x03", "\x04", "\x05", "\x06", "\x07", "\x08", "\t", 
    "\n", "\x0b", "\x0c", "\r", "\x0e", "\x0f", "\x10", "\x11", "\x12", "\x13", 
    "\x14", "\x15", "\x16", "\x17", "\x18", "\x19", "\x1a", "\x1b", "\x1c", 
    "\x1d", "\x1e", "\x1f", " ", "!", '"', "#", "$", "%", "&", "'", "(", ")", 
    "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", 
    "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", 
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
    "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", 
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "\x7f", "\x80", "\x81", 
    "\x82", "\x83", "\x84", "\x85", "\x86", "\x87", "\x88", "\x89", "\x8a", 
    "\x8b", "\x8c", "\x8d", "\x8e", "\x8f", "\x90", "\x91", "\x92", "\x93", 
    "\x94", "\x95", "\x96", "\x97", "\x98", "\x99", "\x9a", "\x9b", "\x9c", 
    "\x9d", "\x9e", "\x9f", "\xa0", "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", 
    "©", "ª", "«", "¬", "\xad", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶", 
    "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", 
    "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", 
    "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", 
    "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", 
    "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷", "ø", "ù", "ú", "û", "ü", 
    "ý", "þ", "ÿ", 
]
SIMPLE_chars = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", 
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "x", "w", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "W", 
    "Y", "Z", "_", " ", 
]

def read_file_as_ascii(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        # converte para ASCII ignorando ou substituindo caracteres que nao sao ASCII
        ascii_content = content.encode("ascii", errors="ignore").decode("ascii")
        return ascii_content
    except Exception as e:
        print(f"Error reading file as ASCII: {e}")
        return None

def save_ascii_data_to_file(ascii_data, file_path):
    try:
        with open(file_path, "w", encoding="ascii") as file:
            file.write(ascii_data)
    except Exception as e:
        print(f"Error saving ASCII data to file: {e}")

def convert_file_to_ascii(input_file_path, output_file_path):
    ascii_data = read_file_as_ascii(input_file_path)
    if ascii_data:
        save_ascii_data_to_file(ascii_data, output_file_path)

def testa_prefixo(a,b):
    prefixo = ''
    for i in range(min(len(a),len(b))): 
            if a[i]==b[i]:
                prefixo += a[i]
            else:
                break
    return prefixo 

def clear_initial_bits(code, n=5):
    reponse = code 
    if len(code) >= n:
        prefix = code[:-n]

        cut_i = 0
        for i in range(len(prefix)):
            if prefix[i] == "0":
                cut_i+=1
            else:
                break
        response = prefix[cut_i:] + code[-n:]
    return response 

class Node:
    def __init__(self, string, is_root=False, is_leaf=True, code = None):
        self.children = []
        self.is_root = is_root
        self.text = string
        self.is_leaf = is_leaf
        self.code = code
        if is_root:
            self.is_leaf = False

    def add_node(self, insere_string, code = None):
        # recebe o texto todo e a string que queremos adicionar
        prefixo = testa_prefixo(self.text, insere_string)

        if prefixo == '' and self.is_root==False:
            pass
        else: 
            if prefixo == self.text:
                if prefixo == insere_string:
                    self.is_leaf = True
                    if self.code is None:
                        self.code = code
                elif len(insere_string) > len(self.text) or self.is_root:
                    sufixo = insere_string[len(prefixo):]
                    if len(self.children) ==0:
                        self.children.append(Node(sufixo, code=code))
                    if len(self.children) !=0 :
                        foi_inserido = False 
                        for i in range(len(self.children)): 
                            prefixo_filho = testa_prefixo(self.children[i].text, sufixo)
                            if prefixo_filho != '':
                                self.children[i].add_node(sufixo, code=code)
                                foi_inserido = True
                        if foi_inserido == False:
                            self.children.append(Node(sufixo,code=code))
            elif len(prefixo) < len(self.text):
                if prefixo == insere_string:
                    sufixo_no_atual = self.text[len(prefixo):]
                    novo_no_atual = Node(sufixo_no_atual, code=self.code)
                    novo_no_atual.children = self.children[::]
                    novo_no_atual.is_leaf = self.is_leaf
                    self.children = []
                    self.children.append(novo_no_atual)
                    self.text = prefixo
                    self.code = code
                else: # prefixo < insere_string
                    sufixo_inserir = insere_string[len(prefixo):] # sufixo do insere_string
                    sufixo_no_atual = self.text[len(prefixo):] # sufixo da string que ta no meu no
                    if len(self.children) == 0:
                        novo_no_atual = Node(sufixo_no_atual, code=self.code)
                        novo_no_inserido = Node(sufixo_inserir, code=code)
                        novo_no_atual.is_leaf = self.is_leaf

                        self.children.append(novo_no_inserido)
                        self.children.append(novo_no_atual)
                        self.text = prefixo
                        self.is_leaf = False
                        self.code = None
                    else: 
                        novo_no_atual = Node(sufixo_no_atual, code=self.code)
                        novo_no_inserido = Node(sufixo_inserir, code=code)
                        novo_no_atual.is_leaf = self.is_leaf

                        novo_no_atual.children = self.children[::]
                        self.children = []
                        self.children.append(novo_no_inserido)
                        self.children.append(novo_no_atual)
                        self.text = prefixo
                        self.is_leaf = False
                        self.code = None

    # pesquisa o codigo 
    def search_code(self, string): 
        response = None
        if self.is_leaf and string == '': 
            response = self.code
        else:
            for i in range(len(self.children)): 
                prefixo = testa_prefixo(string, self.children[i].text)
                if prefixo == self.children[i].text:
                    sufixo = string[len(prefixo):]
                    response = self.children[i].search_code(sufixo)
                    break
                
        return response
            
    # pesquisa a string
    def search(self, string): 
        response = False
        if self.is_leaf and string == '': 
            response = True
        else:
            for i in range(len(self.children)): 
                prefixo = testa_prefixo(string, self.children[i].text)
                if prefixo == self.children[i].text:
                    sufixo = string[len(prefixo):]
                    response = self.children[i].search(sufixo)
                    break
                
        return response

    def n_filhos(self):
        return len(self.children)

        
class Trie : 
    def __init__(self, params_bits=12, is_fixed=True):
        self.root = None
        self.default_bits = params_bits
        self.is_fixed = is_fixed
        self.current_bits = params_bits
        self.max_bits = 2**self.current_bits
        self.current_index = 0

    def initialize_root(self): 
        self.root = Node('', is_root=True)

    def initialize_ascii(self): 
        self.root = Node('', is_root=True)
        for char in ASCII_chars:
            self.add_node(char)

    def initialize_simple(self):
        self.root = Node('', is_root=True)
        for char in SIMPLE_chars:
            self.add_node(char)

    def initialize_simple_reverse(self):
        self.root = Node('', is_root=True)
        for i in range(len(SIMPLE_chars)):
            char = SIMPLE_chars[i]
            code = self.string_bits(i)
            self.add_node_with_code(code, char)

    def initialize_ascii_reverse(self):
        self.root = Node('', is_root=True)
        for i in range(len(ASCII_chars)):
            char = ASCII_chars[i]
            code = self.string_bits(i)
            self.add_node_with_code(code, char)

    def add_node(self, string):
        code = self.current_index 
        if self.current_index >= self.max_bits and self.is_fixed == False:
            self.current_bits = self.current_bits + 1 
            self.max_bits = 2**self.current_bits 
        self.root.add_node(string, code=code)
        self.current_index +=1

    def add_node_with_code(self, string, code):
        if self.current_index >= self.max_bits and self.is_fixed == False:
            self.current_bits = self.current_bits + 1 
            self.max_bits = 2**self.current_bits 
            
        self.root.add_node(string, code=code)
        self.current_index +=1

    def add_node_reversed(self, string):
        code = self.string_bits(self.current_index)
        if self.current_index >= self.max_bits -1 and self.is_fixed == False:
            self.current_bits = self.current_bits + 1 
            self.max_bits = 2**self.current_bits 
        self.root.add_node(code, code=string)
        self.current_index +=1

    def search_node(self, string):
        response = self.root.search(string)
        return response
    
    def search_code(self, string):
        response = self.root.search_code(string)
        return response
    
    def string_bits(self, code): 
        n = None
        if self.is_fixed == True:
            n = self.default_bits
        else: # caso seja falso
            n = self.current_bits

        binary_string = f"{code:0{n}b}"
        return binary_string

# funcao para compressao 
def encode(
    texto,
    params_bits=12,
    is_fixed=True
):
    trie = Trie(params_bits=params_bits, is_fixed=is_fixed)
    trie.initialize_ascii()
    text_encoded = ''
    l = ''
    for i in range(len(texto)):
        x = texto[i]
        conc = l+x 
        code_string = trie.search_code(conc)

        if code_string is None:
            code_l = trie.string_bits(trie.search_code(l))
            text_encoded += code_l
            trie.add_node(conc)
            l = x
        else: 
            l = conc
        if i == len(texto)-1:
            code_l = trie.string_bits(trie.search_code(l))
            text_encoded += code_l
    return text_encoded 

# funcao para descompressao
def decode(
    text_encoded,
    params_bits=12,
    is_fixed=True
):
    texto = text_encoded
    texto_decoded = ''
    trie_reverse = Trie(params_bits=params_bits, is_fixed=is_fixed)
    trie_reverse.initialize_ascii_reverse()
    step = trie_reverse.current_bits

    init = 0
    endt = init + step
    old = clear_initial_bits(texto[init:endt], params_bits)
    S = trie_reverse.search_code(old)
    C = S[0]
    texto_decoded += S

    init += step
    endt = init + step
    while len(texto) >= endt:
        x = clear_initial_bits(texto[init:endt], params_bits)        
        x_code = trie_reverse.search_code(x)
        if x_code is None:
            S = trie_reverse.search_code(old)
            S += C
        else:
            S = x_code
        texto_decoded += S
        C = S[0]
        
        new_code = trie_reverse.search_code(old) + C
        trie_reverse.add_node_reversed(new_code)
        step = trie_reverse.current_bits
        old = x
        
        init = endt
        endt = init + step
    return texto_decoded