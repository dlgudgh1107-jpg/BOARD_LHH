import pymysql

class BoardDAO:

    def __init__(self):
        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = "utf8mb4" #이모티콘

        )
    
    def select_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT * FROM board
        ORDER BY id DESC
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result
    
    def register(self,title,content,writer):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO board (title, content, writer)
        VALUES (%s,%s,%s)
        """

        cursor.execute(sql,(title,content,writer))
        conn.commit()
        cursor.close()
        conn.close()

        print("등록 완료.")

    def select_one(self, board_id):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return result
    
    def update(self,title,content,board_id):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE board
        Set title = %s,
            content = %s
        WHERE id = %s
        """

        cursor.execute(sql, (title,content,board_id))
        conn.commit()
        cursor.close()
        conn.close()

        print("수정 완료.")

    def delete(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))
        conn.commit()
        cursor.close()
        conn.close()

        print("삭제 완료.")

    def comment_all(self, input_id):
        
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT * FROM comment
        WHERE id=%s
        """

        cursor.execute(sql, (input_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result

    def add_comment(self, board_id, content):
        
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO comment (id,content)
        VALUES (%s,%s)
        """
        cursor.execute(sql, (board_id,content))
        conn.commit()
        cursor.close()
        conn.close()

        print("등록 완료.")

    def delete_comment(self, board_id,comm_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM comment
        WHERE id=%s AND commno = %s
        """

        cursor.execute(sql, (board_id,comm_id))
        conn.commit()
        cursor.close()
        conn.close()

        print("삭제 완료.")

    def delete_all_comment(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM comment
        WHERE id=%s
        """

        cursor.execute(sql, (board_id))
        conn.commit()
        cursor.close()
        conn.close()

    def edit_comment(self,content,board_id,commno):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE comment
        Set content = %s
        WHERE id = %s AND commno = %s
        """

        cursor.execute(sql, (content,board_id,commno))
        conn.commit()
        cursor.close()
        conn.close()

        print("수정 완료.")
    
    def comment_one(self, board_id,commno):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            sql = """
            SELECT *
            FROM comment
            WHERE id=%s AND commno=%s
            """

            cursor.execute(sql, (board_id,commno))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            return result
                
        except:
            print("댓글이 존재하지 않습니다. 다시 입력해주세요.")
            return False

