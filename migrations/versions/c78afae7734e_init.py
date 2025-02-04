"""init

Revision ID: c78afae7734e
Revises: 
Create Date: 2025-02-04 00:51:50.566211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c78afae7734e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('precipitation', sa.String(), nullable=False),
    sa.Column('pr_description', sa.String(), nullable=False),
    sa.Column('temp', sa.Float(), nullable=False),
    sa.Column('feels_like', sa.Float(), nullable=False),
    sa.Column('pressure', sa.Integer(), nullable=False),
    sa.Column('humidity', sa.Integer(), nullable=False),
    sa.Column('visibility', sa.Integer(), nullable=False),
    sa.Column('wind_speed', sa.Float(), nullable=False),
    sa.Column('clouds', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('aqi', sa.Integer(), nullable=False),
    sa.Column('co', sa.Float(), nullable=False),
    sa.Column('no', sa.Float(), nullable=False),
    sa.Column('no2', sa.Float(), nullable=False),
    sa.Column('o3', sa.Float(), nullable=False),
    sa.Column('pm10', sa.Float(), nullable=False),
    sa.Column('pm25', sa.Float(), nullable=False),
    sa.Column('so2', sa.Float(), nullable=False),
    sa.Column('nh3', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weather_id'), 'weather', ['id'], unique=False)
    op.create_index(op.f('ix_weather_location'), 'weather', ['location'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_weather_location'), table_name='weather')
    op.drop_index(op.f('ix_weather_id'), table_name='weather')
    op.drop_table('weather')
    # ### end Alembic commands ###
