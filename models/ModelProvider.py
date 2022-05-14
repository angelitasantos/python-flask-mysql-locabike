from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *


class ModelProvider:

    def __init__(self):
        self.grupo = request.form['grupo']
        self.subgrupo = request.form['subgrupo']
        self.nome = request.form['nome']
        self.razaosocial = request.form['razaosocial']
        self.tipo = request.form['tipo']
        self.cnpj = request.form['cnpj']
        self.inscest = request.form['inscest']
        self.cpf = request.form['cpf']
        self.rg = request.form['rg']
        self.endereco = request.form['endereco']
        
        self.numero = request.form['numero']
        self.complemento = request.form['complemento']
        self.bairro = request.form['bairro']
        self.cidade = request.form['cidade']
        self.uf = request.form['uf']
        self.cep = request.form['cep']
        self.telefone1 = request.form['telefone1']
        self.telefone2 = request.form['telefone2']
        self.email = request.form['email']
        self.id = request.form['id']
        self.id_company = request.form['id_company']


    def ProviderRegister(self):
        if request.method == 'POST':
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM providers WHERE email = %s', [self.email])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO providers 
                    (grupo, subgrupo, nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                    bairro, cidade, uf, cep, telefone1, telefone2, email, id_company) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    [self.grupo, self.subgrupo, self.nome, self.razaosocial, self.tipo, 
                    self.cnpj, self.inscest, self.cpf, self.rg, self.endereco, 
                    self.numero, self.complemento, self.bairro, self.cidade, self.uf, 
                    self.cep, self.telefone1, self.telefone2, self.email, self.id_company])
                    mysql.connection.commit()
                    flash('Provider Created Successfully...!!!', 'success')
                else:
                    flash('Provider Found...!!!', 'danger')
            except Exception as e:
                print(e)


    def ProviderUpdate(self):
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute('''UPDATE providers 
            SET grupo = %s, subgrupo = %s, nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
            endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
            uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s, id_company = %s
            WHERE id = %s''',
            [self.grupo, self.subgrupo, self.nome, self.razaosocial, self.tipo, 
            self.cnpj, self.inscest, self.cpf, self.rg, self.endereco, 
            self.numero, self.complemento, self.bairro, self.cidade, self.uf, 
            self.cep, self.telefone1, self.telefone2, self.email, self.id_company, self.id])
            mysql.connection.commit()
            flash("Provider Updated Successfully...!!!", "success")