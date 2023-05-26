"""adding  data

Revision ID: fe3d14f232de
Revises: 2b813cc61b51
Create Date: 2023-05-26 10:51:09.105100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe3d14f232de'
down_revision = '2b813cc61b51'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO public."Cluster"(
        "name")
        VALUES ('Будь аккуратен');
        
        INSERT INTO public."Role"(
        "description","name")
        VALUES ('Главный инженер', 'Андрей');

        INSERT INTO public."User"(
        "name", "surname", "idRole", "position", "login", "passwordHash", "idCluster", "markingDeletion", "createData")
        VALUES ('Аркадий','Капустин','1','Стажёр','1234','12344321','1','true','2023-06-06 14:05:06'),
        ('Акакий','Мольный','1','Профи','1234','12344321','1','true','2023-07-07 14:05:06');

        INSERT INTO public."Project"(
        "name", "description", "idAutor", "createData")
        VALUES ('Печать для музея', 'Струевая печать', '1', '2023-06-16 14:05:06'),
        ('Печать для музея', 'Пучковая печать', '2', '2023-06-16 14:05:06');

        INSERT INTO public."Task"(
        "name", "description", "createData", "idProject") 
        VALUES
        ('Макет вазы', 'Стальная', '2023-06-16 14:05:06', '1'),
        ('Ангелочек', 'Каменная', '2023-06-16 14:05:06', '2');

        """
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM public.tasks CASCADE;
        DELETE FROM public.projects CASCADE;
        DELETE FROM public.users CASCADE;
        DELETE FROM public.clusters CASCADE;
        DELETE FROM public.roles CASCADE;
        """
    )
