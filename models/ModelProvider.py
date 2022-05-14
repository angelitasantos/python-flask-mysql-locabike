from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *


class ModelProvider:

    def __init__(self) -> None:
        pass


    def ProviderRegister(self):
        if request.method == 'POST':
            grupo = request.form['grupo']
            subgrupo = request.form['subgrupo']
            nome = request.form['nome']
            razaosocial = request.form['razaosocial']
            tipo = request.form['tipo']
            cnpj = request.form['cnpj']
            inscest = request.form['inscest']
            cpf = request.form['cpf']
            rg = request.form['rg']
            endereco = request.form['endereco']
            numero = request.form['numero']
            complemento = request.form['complemento']
            
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            uf = request.form['uf']
            cep = request.form['cep']
            telefone1 = request.form['telefone1']
            telefone2 = request.form['telefone2']
            email = request.form['email']
            id_company = request.form['id_company']

            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM providers WHERE email = %s', [email])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO providers 
                    (grupo, subgrupo, nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email, id_company) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    [grupo, subgrupo, nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email, id_company])
                    mysql.connection.commit()
                    flash('Provider Created Successfully...!!!', 'success')
                else:
                    flash('Provider Found...!!!', 'danger')
            except Exception as e:
                print(e)


    def ProviderUpdate(self):
        if request.method == 'POST':
            grupo = request.form['grupo']
            subgrupo = request.form['subgrupo']
            nome = request.form['nome']
            razaosocial = request.form['razaosocial']
            tipo = request.form['tipo']
            cnpj = request.form['cnpj']
            inscest = request.form['inscest']
            cpf = request.form['cpf']
            rg = request.form['rg']
            endereco = request.form['endereco']
            numero = request.form['numero']
            complemento = request.form['complemento']
            
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            uf = request.form['uf']
            cep = request.form['cep']
            telefone1 = request.form['telefone1']
            telefone2 = request.form['telefone2']
            email = request.form['email']
            id = request.form['id']
            id_company = request.form['id_company']
            
            cursor = mysql.connection.cursor()
            cursor.execute('''UPDATE providers 
            SET grupo = %s, subgrupo = %s, nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
            endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
            uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s, id_company = %s
            WHERE id = %s''',
            [grupo, subgrupo, nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
            bairro, cidade, uf, cep, telefone1, telefone2, email, id_company, id])
            mysql.connection.commit()
            flash("Provider Updated Successfully...!!!", "success")