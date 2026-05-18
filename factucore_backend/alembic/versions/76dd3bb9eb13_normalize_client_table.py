"""normalize client table

Revision ID: 76dd3bb9eb13
Revises: 047338e31777
Create Date: 2026-05-18 14:04:51.420054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '76dd3bb9eb13'
down_revision: Union[str, Sequence[str], None] = '047338e31777'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('cliente', sa.Column('cli_apellido', sqlmodel.sql.sqltypes.AutoString(length=80), nullable=False))
    op.alter_column(
        'cliente',
        'fono',
        existing_type=sa.VARCHAR(length=25),
        existing_nullable=False,
        new_column_name='cli_telefono',
    )
    op.alter_column(
        'cliente',
        'direccion',
        existing_type=sa.VARCHAR(length=55),
        existing_nullable=False,
        new_column_name='cli_direccion',
    )
    op.alter_column(
        'cliente',
        'c_descripcion',
        existing_type=sa.VARCHAR(length=45),
        existing_nullable=False,
        new_column_name='cli_descripcion',
    )
    op.create_unique_constraint('uq_cliente_cedula', 'cliente', ['cedula'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('uq_cliente_cedula', 'cliente', type_='unique')
    op.alter_column(
        'cliente',
        'cli_descripcion',
        existing_type=sa.VARCHAR(length=45),
        existing_nullable=False,
        new_column_name='c_descripcion',
    )
    op.alter_column(
        'cliente',
        'cli_direccion',
        existing_type=sa.VARCHAR(length=55),
        existing_nullable=False,
        new_column_name='direccion',
    )
    op.alter_column(
        'cliente',
        'cli_telefono',
        existing_type=sa.VARCHAR(length=25),
        existing_nullable=False,
        new_column_name='fono',
    )
    op.drop_column('cliente', 'cli_apellido')
