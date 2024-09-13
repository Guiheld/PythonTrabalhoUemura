Ciencias da Computação - Tópicos Especiais em Software - Professor Marcelo Takashi Uemura

Trabalho A2 - 2,5
Sistema de Gerenciamento de Tarefas Web

Integrantes do grupo:
  Guilherme Azevedo Held
  Luciano Moliani
  Luiz Felipe Hoffman

INSTRUÇÕES


  Após importar o projeto, navegue pelo terminal em sua IDE até o diretório "TrabalhoUemura" e execute os seguintes comandos para a migração
    1. python manage.py makemigrations
    2. python manage.py migrate

  Em seguida, execute o comando abaixo para rodar o projeto 
       python manage.py runserver

  Certifique-se que voce possue o framework Django baixado, caso nao, rode o seguinte comando
       pip install django


  1. Cadastro de Usuários + Logina
         Ao acessar a URL do projeto, o usuário é redirecionado para a tela de login. Caso o usuário não possua uma conta, há um link disponível abaixo para a página de cadastro.
       Para se cadastrar, é necessário preencher os campos Nome, Email e Senha. Após concluir o cadastro, o usuário é redirecionado novamente para a tela de login, onde poderá inserir suas credenciais e ser autenticado.

  2. Gerenciamento de Tarefas
       2.1 Minhas Tarefas
             Uma vez autenticado, o usuário será direcionado para a página "Minhas Tarefas", onde é possível visualizar as tarefas atribuídas a ele, cadastrar novas tarefas, acessar o dashboard, editar e/ou excluir tarefas existentes.
           A página "Minhas Tarefas" tem o intuito de permitir o usuário visualizar as tarefas designadas a ele e administrá-las, podendo também filtrá-las por andamento/status (pendente, em andamento e concluída).
     
       2.2 Dashboard
             A página "Dashboard" permite que todos os usuários visualizem todas as tarefas cadastradas, organizadas por usuários atribuídos a elas em filas. Também é possível editar e excluir tarefas pelo dashboard, assim como na página "Minhas Tarefas".
           Além disso, a página oferece botões para fazer logoff (sair) e voltar.
     
       2.3 Criar uma tarefa nova
             Na página "Criar Tarefa", o usuário deve fornecer informações básicas para cadastrar uma nova tarefa, incluindo Título, Descrição, Status e Responsável. Com esses dados, a nova tarefa é criada e associada ao ID do usuário que a criou.

       2.4 Exclusão de uma tarefa
             Em ambas as páginas, é possível excluir uma tarefa. Ao clicar no botão vermelho, o usuário é redirecionado para uma página de confirmação. Nessa página, todas as informações sobre a tarefa são exibidas e são disponibilizadas duas opções: confirmar ou cancelar a exclusão.

SOBRE O CODIGO:
      O codigo segue o padrão do framework django, contendo as rotas em urls.py, regras de negocio em views.py e os templates html no diretorio /templates/. 
    
    1. Autenticação 
  
      A função de cadastro do sistema utiliza tanto o modelo padrão do Django (User) quanto um modelo personalizado (Usuarios). O modelo padrão do Django é usado para uma implementação rápida e segura, aproveitando as funcionalidades prontas do framework. 
    Por outro lado, o modelo personalizado permite a customização necessária para atender a requisitos específicos do projeto.
    
      Para a função de login, o sistema utiliza exclusivamente o método padrão do Django (login(request, user)). Isso é feito devido à superior segurança e facilidade de implementação oferecidas pelo sistema de autenticação padrão,
    especialmente com relação à automatização do hash de senhas.
    
  Gerenciamento de Tarefas (Criação, Remoção, Edição e Visualização)
  
    2. Visualização
        Após a autenticação, o usuário é redirecionado do login para a função "definir_tarefa", onde são aplicadas as regras de negócios da página "Minhas Tarefas". 
      Nessa função, o sistema busca o objeto do usuário atualmente logado e suas tarefas (aquelas atribuídas a ele, e não as criadas por ele).
      Em seguida, a página HTML é renderizada. Um loop é utilizado para criar um cartão para cada tarefa, listando seus dados. 
      No final do arquivo, há um script em JavaScript que implementa a lógica de filtragem das tarefas com base no seu status/andamento.
      
        A função dashboard pode ser acessada a partir da página "Minhas Tarefas" através de um botão. Nessa função, são buscados todos os usuários e criado um dicionário que mapeia cada usuário para as suas tarefas. 
      Em seguida, a página HTML é renderizada, que é semelhante à página "Minhas Tarefas".

    3. Criação
        A função de criação de tarefas utiliza um formulário definido em formulario.py. Após o usuário preenchê-lo, é criado um objeto de tarefa e o usuário logado é buscado para finalizar a criação da nova tarefa.
      Para criar o formulário, é realizado um query para buscar todos os usuários e uma lista de possiveis valores para "status", o que popula o campo de opções para selecionar o responsável e o status atual da tarefa pela nova tarefa.
      
    4. Exclusão
        A função de exclusão recebe como parâmetro o id da tarefa a ser deletada. Então, a tarefa é buscada e deletada.
      A diferença entre as funções "deletar_tarefa" e "deletar_tarefa_dashboard" é que na função "deletar_tarefa_dashboard" o usuário logado não é buscado.
      
    5. Atualizar/Editar
       A função de editar/atualizar a tarefa foi feita com a lógica semelhante a de exclusão, porém invez de deletar, o usuario é encaminhado para o formulario, onde ele é preenchido novamente e então as alterações são salvas.
      A única diferença entre "atualizar_tarefa" e "atualizar_tarefa_dashboard" também é a mesma que em exclusão, em "atualizar_tarefa_dashboard" não tem uma busca pelo usuario.

Observação: A função "home" serve somente para redirecionar o usuaro à tela de login.
        
  
