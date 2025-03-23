from src.db.database import connection_pool
from src.models.job import Job

class JobsRepository:
    @staticmethod
    def create_job(title: str, description: str) -> Job:
        conn = connection_pool.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO jobs (title, description)
                VALUES (%s, %s)
                """,
                (title, description),
            )
            job_id = cursor.lastrowid
            conn.commit()


            cursor.execute("SELECT created_at, updated_at FROM jobs WHERE id = %s", (job_id,))
            created_at, updated_at = cursor.fetchone()

            return Job(job_id, title, description, created_at, updated_at)

        except Exception as e:
            conn.rollback()
            raise e

        finally:
            cursor.close()
            conn.close()
