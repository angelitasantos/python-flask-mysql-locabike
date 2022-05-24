from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from models.Form import *

def BrandRegister():
    form = ModelFormGroup()
    if request.method == 'POST':
        description = form.description.data.upper()

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM brands WHERE description = %s', [description])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO brands 
                (description) 
                VALUES (%s)''',
                [description])
                mysql.connection.commit()
                flash('Brand Created Successfully...!!!', 'success')
            else:
                flash('Brand Found...!!!', 'danger')
        except Exception as error:
            print(error)


def BrandUpdate():
    form = ModelFormGroup()
    if request.method == 'POST':
        description = form.nome.description.upper()
        id = form.id.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE brands 
        SET description = %s
        WHERE id = %s''',
        [description, id])
        mysql.connection.commit()
        flash("Brand Updated Successfully...!!!", "success")

    
def CategoryRegister():
    form = ModelFormGroup()
    if request.method == 'POST':
        description = form.description.data.upper()

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM categories WHERE description = %s', [description])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO categories 
                (description) 
                VALUES (%s)''',
                [description])
                mysql.connection.commit()
                flash('Category Created Successfully...!!!', 'success')
            else:
                flash('Category Found...!!!', 'danger')
        except Exception as error:
            print(error)


def CategoryUpdate():
    form = ModelFormGroup()
    if request.method == 'POST':
        description = form.nome.description.upper()
        id = form.id.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE categories 
        SET description = %s
        WHERE id = %s''',
        [description, id])
        mysql.connection.commit()
        flash("Category Updated Successfully...!!!", "success")


def ProductRegister():
    form = ModelFormProduct()
    if request.method == 'POST':
        name = form.name.data.upper()
        description = form.description.data.upper()
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        image = form.image.data
        id_brand = form.id_brand.data
        id_category = form.id_category.data
        id_company = form.id_company.data

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM products WHERE name = %s', [name])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO products 
                (name, description, price, discount, stock, colors, image, id_brand, id_category, id_company) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                [name, description, price, discount, stock, colors, image ,id_brand, id_category, id_company])
                mysql.connection.commit()
                flash('Product Created Successfully...!!!', 'success')
            else:
                flash('Product Found...!!!', 'danger')
        except Exception as error:
            print(error)


def ProductUpdate():
    form = ModelFormProduct()
    if request.method == 'POST':
        name = form.name.data.upper()
        description = form.description.data.upper()
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        id = form.id.data
        id_company = form.id_company.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE products 
        SET name = %s, description = %s, price = %s, 
        discount = %s, stock = %s, colors = %s, id_company = %s
        WHERE id = %s''',
        [name, description, price, discount, stock, colors, id_company, id])
        mysql.connection.commit()
        flash("Product Updated Successfully...!!!", "success")