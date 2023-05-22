# pylint: disable=invalid-name,no-member
"""initialize secret

Revision ID: b3d87e360774
Revises: 
Create Date: 2023-05-21 21:55:26.760272

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "b3d87e360774"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "secret",
        sa.Column("secret_data", sa.LargeBinary(), nullable=False),
        sa.Column("salt", sa.LargeBinary(), nullable=False),
        sa.Column("id", sa.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_secret_created_at"), "secret", ["created_at"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_secret_created_at"), table_name="secret")
    op.drop_table("secret")
    # ### end Alembic commands ###
