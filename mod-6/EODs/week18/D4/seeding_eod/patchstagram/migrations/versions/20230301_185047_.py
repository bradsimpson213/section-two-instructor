"""create users, posts, and likes tables

Revision ID: fd2504195396
Revises: 
Create Date: 2023-03-01 18:50:47.004521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd2504195396'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('profile_pic', sa.String(length=250), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caption', sa.String(length=255), nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('post_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('users', sa.Integer(), nullable=False),
    sa.Column('posts', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['users'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users', 'posts')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###
