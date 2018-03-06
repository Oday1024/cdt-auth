"""nullable false4

Revision ID: 0f915ee2e639
Revises: 6f2cacbae725
Create Date: 2018-03-06 22:46:17.083840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f915ee2e639'
down_revision = '6f2cacbae725'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('td_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('log_time', sa.DateTime(), nullable=True),
    sa.Column('account', sa.String(length=128), nullable=True),
    sa.Column('res_id', sa.String(length=128), nullable=True),
    sa.Column('res_path', sa.String(length=128), nullable=True),
    sa.Column('sys_res_id', sa.String(length=128), nullable=True),
    sa.Column('sys_res_name', sa.String(length=128), nullable=True),
    sa.Column('sys_res_path', sa.String(length=128), nullable=True),
    sa.Column('page_res_id', sa.String(length=128), nullable=True),
    sa.Column('page_res_name', sa.String(length=128), nullable=True),
    sa.Column('page_res_path', sa.String(length=128), nullable=True),
    sa.Column('func_res_id', sa.String(length=128), nullable=True),
    sa.Column('func_res_name', sa.String(length=128), nullable=True),
    sa.Column('func_res_path', sa.String(length=128), nullable=True),
    sa.Column('params', sa.String(length=128), nullable=True),
    sa.Column('log_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_id', sa.String(length=128), nullable=True),
    sa.Column('menu_name', sa.String(length=128), nullable=True),
    sa.Column('menu_res_path', sa.String(length=128), nullable=True),
    sa.Column('p_menu_id', sa.String(length=128), nullable=True),
    sa.Column('sys_res_id', sa.String(length=128), nullable=True),
    sa.Column('sys_res_name', sa.String(length=128), nullable=True),
    sa.Column('sys_res_path', sa.String(length=128), nullable=True),
    sa.Column('page_res_id', sa.String(length=128), nullable=True),
    sa.Column('page_res_name', sa.String(length=128), nullable=True),
    sa.Column('page_res_path', sa.String(length=128), nullable=True),
    sa.Column('sort_id', sa.Integer(), nullable=True),
    sa.Column('icon', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_res',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('res_id', sa.String(length=128), nullable=True),
    sa.Column('res_name', sa.String(length=128), nullable=True),
    sa.Column('func_name', sa.String(length=128), nullable=True),
    sa.Column('res_flag', sa.String(length=128), nullable=True),
    sa.Column('res_path', sa.String(length=128), nullable=True),
    sa.Column('res_type_id', sa.Integer(), nullable=True),
    sa.Column('res_type', sa.String(length=128), nullable=True),
    sa.Column('p_res_id', sa.String(length=128), nullable=True),
    sa.Column('p_res_name', sa.String(length=128), nullable=True),
    sa.Column('api_url', sa.String(length=128), nullable=True),
    sa.Column('sys_res_id', sa.String(length=128), nullable=True),
    sa.Column('sys_res_name', sa.String(length=128), nullable=True),
    sa.Column('sys_name', sa.String(length=128), nullable=True),
    sa.Column('sys_flag', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('updater', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('creater', sa.String(length=128), nullable=True),
    sa.Column('data_access_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_res_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('res_type', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('res_type'),
    schema='sys'
    )
    op.create_table('td_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.String(length=128), nullable=True),
    sa.Column('role_name', sa.String(length=128), nullable=True),
    sa.Column('data_scope', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('b_inside', sa.Integer(), nullable=True),
    sa.Column('b_super', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('updater', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('creater', sa.String(length=128), nullable=True),
    sa.Column('data_role', sa.String(length=128), nullable=True),
    sa.Column('data_access_level', sa.Integer(), nullable=True),
    sa.Column('inside_default_open_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_role_res',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.String(length=128), nullable=True),
    sa.Column('res_id', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('updater', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('creater', sa.String(length=128), nullable=True),
    sa.Column('data_role', sa.String(length=128), nullable=True),
    sa.Column('data_access_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_role_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.String(length=128), nullable=True),
    sa.Column('open_id', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('updater', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('creater', sa.String(length=128), nullable=True),
    sa.Column('data_role', sa.String(length=128), nullable=True),
    sa.Column('data_access_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    op.create_table('td_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('open_id', sa.String(length=128), nullable=False),
    sa.Column('account', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('b_inside', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('updater', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('creater', sa.String(length=128), nullable=True),
    sa.Column('data_role', sa.String(length=128), nullable=True),
    sa.Column('data_access_level', sa.Integer(), nullable=True),
    sa.Column('inside_default_role_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='sys'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('td_user', schema='sys')
    op.drop_table('td_role_user', schema='sys')
    op.drop_table('td_role_res', schema='sys')
    op.drop_table('td_role', schema='sys')
    op.drop_table('td_res_type', schema='sys')
    op.drop_table('td_res', schema='sys')
    op.drop_table('td_menu', schema='sys')
    op.drop_table('td_log', schema='sys')
    # ### end Alembic commands ###
