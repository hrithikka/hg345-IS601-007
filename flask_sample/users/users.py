from flask import Blueprint, redirect, request, render_template, url_for, flash, Flask, request, jsonify, session
import requests
from sql.db import DB
from roles.permissions import admin_permission

users = Blueprint('users', __name__, url_prefix='/users',
                  template_folder="templates")


@users.route('/', methods=['GET'])
@admin_permission.require(http_exception=403)
def list_users():
    user_id = session.get('_user_id')
    print("User ID", user_id)

    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401
    users = DB.selectAll(
        "SELECT * FROM IS601_Users")
    admin_users = DB.selectAll(
        "SELECT user_id from IS601_UserRoles where role_id = -1 ")
    admin_user_ids = [admin_user['user_id'] for admin_user in admin_users.rows]

    final_users = []

    for user in users.rows:
        if str(user.get("id")) == str(user_id):
            continue
        if user.get("id") in admin_user_ids:
            user["is_admin"] = True
        else:
            user["is_admin"] = False
        final_users.append(user)

    return render_template('users_list.html', users_list=final_users)


@users.route('/<string:id>', methods=['POST'])
@admin_permission.require(http_exception=403)
def add_as_admin(id):
    user_id = session.get('_user_id')

    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401

    favorite = DB.insertOne(
        "INSERT INTO IS601_UserRoles (user_id, role_id, is_active) VALUES (%s, -1, true)",
        id)

    return jsonify({"message": "Added as a favourite"}), 200


@users.route('/<string:id>', methods=['DELETE'])
@admin_permission.require(http_exception=403)
def remove_as_admin(id):
    user_id = session.get('_user_id')
    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401

    delete_favourite = DB.delete(
        "delete FROM IS601_UserRoles WHERE user_id = %s", id)
    return jsonify({"message": "Deleted"}), 204
