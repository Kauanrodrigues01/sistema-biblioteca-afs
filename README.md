# Sistema de Biblioteca - EEEP Adolfo Ferreira de Sousa

<p align="center">
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/sistema-biblioteca-afs/imagem-consulta-acervo.png" alt="Consulta ao Acervo" width="400"/>
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/sistema-biblioteca-afs/imagem-emprestimos.png" alt="Empréstimos" width="400"/> 
</p>

Sistema de gerenciamento de biblioteca desenvolvido para a EEEP Adolfo Ferreira de Sousa, com funcionalidades completas para administração do acervo e controle de empréstimos.

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Funcionalidades

- **CRUD completo de livros** - Cadastro, leitura, atualização e remoção de títulos do acervo
- **Sistema de empréstimos** - Controle completo dos empréstimos de livros
- **Autenticação de usuários** - Sistema de login seguro
- **Pesquisa de livros** - Busca eficiente no acervo
- **Impressão de cartão de empréstimo** - Geração de comprovante de empréstimo
- **Sistema visual de status**:
  - 🟢 Verde - Empréstimo em dia
  - 🟡 Amarelo - Dia de devolução
  - 🔴 Vermelho - Atrasado
- **Relatório de atrasos** - Impressão de lista com alunos com livros atrasados

## Pré-requisitos

- Docker e Docker Compose instalados

## Como Executar o Projeto

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca.git
   cd sistema-biblioteca
   ```

2. Configure as variáveis de ambiente no arquivo .env:
```text
# SECRET_KEY='django-insecure-ej)ukksy3om#1^p7s#o(m27c4i-5d6frboyhdlfg-!_u+7f5zb'
# DEBUG=True
# ALLOWED_HOSTS=*
# LANGUAGE_CODE='pt-br'
# TIME_ZONE='America/Sao_Paulo'
ADMIN_USERNAME='dev'
ADMIN_PASSWORD='1234'
```

3. Inicie os containers com Docker:
```bash
docker compose up -d
```

4. Acesse a aplicação:
```
http://localhost:8000
```

---

#### Desenvolvido para a EEEP Adolfo Ferreira de Sousa - © 2025

<br>
