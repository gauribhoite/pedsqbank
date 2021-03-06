"""empty message

Revision ID: 6b47ddde7d68
Revises: 10a9a76125ac
Create Date: 2017-04-25 22:57:54.683788

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6b47ddde7d68'
down_revision = '10a9a76125ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('correct', sa.Boolean(), nullable=True))
    op.drop_column('question', 'solution')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('solution', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('question', 'correct')
    # ### end Alembic commands ###
