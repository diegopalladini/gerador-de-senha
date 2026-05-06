from flask import Flask, render_template, request
import secrets
import string

def gerar_senha(tamanho=12, usar_mai=True, usar_min=True, usar_num=True, usar_simb=True):
    # caracteres = string.ascii_letters + string.digits + string.punctuation (essa linha libera usar todos os caracteres)

    caracteres = ""
    if usar_mai: caracteres += string.ascii_uppercase
    if usar_min: caracteres += string.ascii_lowercase
    if usar_num: caracteres += string.digits
    if usar_simb: caracteres += string.punctuation

    # Caso o usuário desmarque tudo, retornamos um aviso ou um padrão
    if not caracteres:
        return "Selecione ao menos uma opção."

    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    return senha
 

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    senha_gerada = ""
    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho', 12))
        
        # O request.form.get retorna o valor ou None se não estiver marcado
        usar_mai = request.form.get('letras_mai') == 'on'
        usar_min = request.form.get('letras_min') == 'on'
        usar_num = request.form.get('numeros') == 'on'
        usar_simb = request.form.get('simbolos') == 'on'
        
        senha_gerada = gerar_senha(tamanho, usar_mai, usar_min, usar_num, usar_simb)
    
    return render_template('index.html', senha=senha_gerada)

if __name__ == '__main__':
    app.run()
