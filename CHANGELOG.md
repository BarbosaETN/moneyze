# Changelog

Todas as mudanças relevantes do **MoneyZe** serão documentadas neste arquivo.

O formato segue o padrão de **Semantic Versioning (SemVer)**:

- **MAJOR** — mudanças incompatíveis ou grandes alterações no projeto.
- **MINOR** — novas funcionalidades compatíveis.
- **PATCH** — correções e ajustes.

---

## [1.0.0] - 2026-09-14

### Adicionado

- Controle de receitas.
- Controle de despesas.
- Cadastro e gerenciamento de categorias.
- Histórico de transações.
- Filtros no histórico por:
  - Tipo de transação.
  - Período.
  - Categoria.
  - Pesquisa.
  - Combinação de filtros.
- Dashboard financeiro.
- Visualização de:
  - Total de receitas.
  - Total de despesas.
  - Saldo.
  - Movimentações financeiras.
- Relatórios e análises financeiras.
- Comparação mensal.
- Distribuição de despesas por categoria.
- Evolução do saldo.
- Configurações do aplicativo.
- Personalização do nome do usuário.
- Seleção de tema:
  - Claro.
  - Escuro.
  - Sistema.
- Configuração de moeda.
- Persistência das configurações.
- Backup do banco de dados.
- Restauração do banco de dados.
- Validação de integridade do banco durante backup e restauração.
- Persistência dos dados utilizando SQLite.
- Arquitetura organizada em:
  - Views.
  - Services.
  - Repositories.
  - Models.
- Sistema de tratamento de erros e mensagens para operações inválidas.
- Atualização automática das telas após alterações nas transações.
- Aplicativo desktop desenvolvido com PySide6.
- Empacotamento do aplicativo para Windows utilizando PyInstaller.
- Ícone personalizado do MoneyZe.
- README completo com documentação do projeto.
- Screenshots das principais telas da aplicação.

### Qualidade e estabilidade

- Testes dos fluxos de criação e exclusão de receitas.
- Testes dos fluxos de criação e exclusão de despesas.
- Testes de criação, consulta e exclusão de categorias.
- Testes de persistência após reinicialização do aplicativo.
- Testes dos cálculos de receitas, despesas e saldo.
- Testes de filtros do histórico.
- Testes de precisão monetária.
- Testes de propagação das alterações entre Dashboard, Histórico e Relatórios.
- Testes de backup e restauração.
- Testes de tratamento de erros.
- Revisão visual das principais telas.
- Teste final do executável em outro computador.

### Fora do MVP

As seguintes funcionalidades não fazem parte da versão 1.0.0:

- Edição de transações.
- Gráficos avançados.
- Sincronização em nuvem.
- Integração com bancos.
- Aplicativo mobile.
- Sistema multiusuário.

### Status

**Release 1.0.0 — MVP concluído e pronto para uso.**

---

## Próximas versões

### [1.0.1] - Futuro

Versão destinada a correções de bugs e pequenos ajustes, sem introdução de grandes funcionalidades.

### [1.1.0] - Futuro

Versão destinada à introdução de novas funcionalidades compatíveis com a arquitetura atual.

### [2.0.0] - Futuro

Versão destinada a mudanças maiores na aplicação que possam alterar significativamente sua arquitetura ou funcionamento.

---

[1.0.0]: https://github.com/BarbosaETN/MoneyZe/releases/tag/v1.0.0