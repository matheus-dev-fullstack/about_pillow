from PIL import Image

imagem = Image.open("imagens/ciri.png")

# Necessário para converter de png para jpg
imagem_rgb = imagem.convert("RGB")

# Alterado o formato
imagem_rgb.save("imagens/ciri.jpg")

# Converter o tamanho
tamanho = (100, 100)

# Muda o tamanho e mantêm a proporção
imagem.thumbnail(tamanho) 

imagem.save("imagens/ciri 100x100.png")

