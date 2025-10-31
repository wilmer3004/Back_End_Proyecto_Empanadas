from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Report_Model import Report_Model
from src.database.database import get_db_conecction

class Report_Service(Crud_Interface):
    
    # Consult all reports
    @classmethod
    def consult(cls):
        try:
            connection = get_db_conecction()
            reports = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM report")
                result = cursor.fetchall()
                for row in result:
                    report = Report_Model(row[0], row[1], row[2], row[3], row[4], row[5])
                    reports.append(report.to_dict())
            connection.commit()
            return reports
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve reports", "code": 500}
        finally:
            connection.close()

    # Create a new report
    @classmethod
    def create(cls, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO report (id_report_type_fk, id_user_fk, date_report, description_report)
                    VALUES (%s, %s, %s, %s)
                """
                data_tuple = (
                    data["id_report_type_fk"],
                    data["id_user_fk"],
                    data["date_report"],
                    data["detail_report"]
                )
                cursor.execute(sql, data_tuple)
            connection.commit()
            return {"message": "Report created successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to insert report", "code": 500}
        finally:
            connection.close()

    # Consult a report by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM report WHERE id_report = %s"
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    report = Report_Model(row[0], row[1], row[2], row[3], row[4], row[5])
                    return report.to_dict()
                return {"error": "Report not found", "code": 404}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve report", "code": 500}
        finally:
            connection.close()

    # Update report details
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    UPDATE report 
                    SET id_report_type_fk = %s, id_user_fk = %s, date_report = %s, description_report = %s
                    WHERE id_report = %s
                """
                data_tuple = (
                    data["id_report_type_fk"],
                    data["id_user_fk"],
                    data["date_report"],
                    data["detail_report"],
                    id
                )
                cursor.execute(sql, data_tuple)
            connection.commit()
            if cursor.rowcount == 0:
                return {"error": "Report not found", "code": 404}
            return {"message": "Report updated successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to update report", "code": 500}
        finally:
            connection.close()

    # Change report state (activate/deactivate)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql_check = "SELECT state_report FROM report WHERE id_report = %s"
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()
                if not row:
                    return {"error": "Report not found", "code": 404}
                current_state = row[0]
                new_state = not current_state
                sql = "UPDATE report SET state_report = %s WHERE id_report = %s"
                cursor.execute(sql, (new_state, id))
            connection.commit()
            return {"message": "Report state changed successfully", "new_state": new_state}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to change report state", "code": 500}
        finally:
            connection.close()
