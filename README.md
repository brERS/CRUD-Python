# Crud in Python
> Projeto usa o mysql-connector para realizar a conexão, possui validação no where e sistema de log das ações 

<br/>

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
- Python3.8 ou superior
  - Modulo mysql-connector
- mysql-server ou mariadb

#

## 🚀 Instalando CRUD-Python

Para instalar o CRUD-Python, siga estas etapas:

- Crie o banco de teste
  ```
  CREATE DATABASE teste_crud CHARACTER SET UTF8mb4 COLLATE utf8mb4_0900_ai_ci;
  ```

- Crie e tabela no banco de teste
  ```
  USE teste_crud;
  ```
  ```
  CREATE TABLE `crudpython`  (
    `crudid` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
    `sobrenome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
    `to_date` datetime NULL DEFAULT NULL,
    PRIMARY KEY (`crudid`) USING BTREE
  ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
  ```

- Crie um usuário e de as permissões para realizar o teste
  ```
  CREATE USER 'crudteste'@'localhost' IDENTIFIED WITH mysql_native_password BY 'passcrudteste';
  ```
  ```
  GRANT SELECT, INSERT, DELETE, UPDATE ON teste_crud.* TO crudteste@'localhost';
  ```
  ```
  FLUSH PRIVILEGES;
  ```
#

## :information_source: Usando CRUD-Python

Para usar CRUD-Python, siga estas etapas:

- Crie o diretório de log na raiz do projeto
  ```
  sudo mkdir log
  ```
- Execute o arquivo para realizar as ações CRUD
  ```
  sudo python3 validate_crud.py
  ```

## :information_source: Validando o Log

Para validar o log, siga estas etapas:

- Verifique se os arquivos de log create_db.log, update_db.log e delete_db.log foram criados e populados
  ```
   tail -f log/*.log
  ```
- Para validar o arquivo de log read_db.log você terá de forçar uma falha na consulta
  ```
   sudo sed -i "s/*/forçar_falha/g" validate_crud.py
  ```
  ```
  sudo python3 validate_crud.py
  ```
  Depois de validar, desfaça a alteração
  ```
  sudo sed -i "s/forçar_falha/*/g" validate_crud.py
  ``` 
- Para validar o arquivo de log connect_db_error.log vc tera de força uma falha na connexão com o banco
  ```
   sudo sed -i "s/'database':'teste_crud'/'database':'forçar_falha'/g" crud.py
  ```
  ```
  sudo python3 validate_crud.py
  ```
  Depois de validar, desfaça a alteração
  ```
  sudo sed -i "s/'database':'forçar_falha'/'database':'teste_crud'/g" crud.py
  ``` 
