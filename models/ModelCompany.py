from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *


class ModelCompany:

    def __init__(self) -> None:
        pass


    def CompanyRegister(self):
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

            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM companies WHERE email = %s', [email])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO companies 
                    (nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    [nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email])
                    mysql.connection.commit()
                    flash('Company Created Successfully...!!!', 'success')
                else:
                    flash('Company Found...!!!', 'danger')
            except Exception as e:
                print(e)