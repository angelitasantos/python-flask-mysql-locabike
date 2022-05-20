from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from models.Form import *


def StoreRegister():
    form = ModelFormPeople()
    if request.method == 'POST':
        nome = form.nome.data.upper()
        razaosocial = form.razaosocial.data.upper()
        tipo = form.tipo.data.upper()
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data.upper()
        endereco = form.endereco.data.upper()
        
        numero = form.numero.data.upper()
        complemento = form.complemento.data.upper()
        bairro = form.bairro.data.upper()
        cidade = form.cidade.data.upper()
        uf = form.uf.data.upper()
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data.lower()
        id_company = form.id_company.data

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
                [nome, razaosocial, tipo, cnpj, inscest, 
                cpf, rg, endereco, numero, complemento,
                bairro, cidade, uf, cep, telefone1, 
                telefone2, email, id_company])
                mysql.connection.commit()
                flash('Store Created Successfully...!!!', 'success')
            else:
                flash('Store Found...!!!', 'danger')
        except Exception as error:
            print(error)


def StoreUpdate():
    form = ModelFormPeople()
    if request.method == 'POST':
        nome = form.nome.data.upper()
        razaosocial = form.razaosocial.data.upper()
        tipo = form.tipo.data.upper()
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data.upper()
        endereco = form.endereco.data.upper()
        
        numero = form.numero.data.upper()
        complemento = form.complemento.data.upper()
        bairro = form.bairro.data.upper()
        cidade = form.cidade.data.upper()
        uf = form.uf.data.upper()
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data.lower()
        id = form.id.data
        id_company = form.id_company.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE stores 
        SET nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
        endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
        uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s, id_company = %s
        WHERE id = %s''',
        [nome, razaosocial, tipo, cnpj, inscest, 
        cpf, rg, endereco, numero, complemento,
        bairro, cidade, uf, cep, telefone1, 
        telefone2, email, id_company, id])
        mysql.connection.commit()
        flash("Store Updated Successfully...!!!", "success")