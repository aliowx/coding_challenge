"""add processing_time and tracker_id

Revision ID: df2350c049e9
Revises: 07ea1a401dc0
Create Date: 2024-04-09 16:13:14.505813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df2350c049e9'
down_revision = '07ea1a401dc0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requestlog', sa.Column('processing_time', sa.Float(), nullable=True))
    op.add_column('requestlog', sa.Column('tracker_id', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requestlog', 'tracker_id')
    op.drop_column('requestlog', 'processing_time')
    # ### end Alembic commands ###
