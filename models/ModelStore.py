from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *


class ModelStore:

    def __init__(self) -> None:
        pass


    def StoreRegister(self):
        if request.method == 'POST':
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
                cursor.execute('SELECT * FROM stores WHERE email = %s', [email])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO stores 
                    (nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email, id_company) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    [nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email, id_company])
                    mysql.connection.commit()
                    flash('Store Created Successfully...!!!', 'success')
                else:
                    flash('Store Found...!!!', 'danger')
            except Exception as e:
                print(e)


    def StoreUpdate(self):
        if request.method == 'POST':
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
            cursor.execute('''UPDATE stores 
            SET nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
            endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
            uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s, id_company = %s
            WHERE id = %s''',
            [nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
            bairro, cidade, uf, cep, telefone1, telefone2, email, id_company, id])
            mysql.connection.commit()
            flash("Store Updated Successfully...!!!", "success")