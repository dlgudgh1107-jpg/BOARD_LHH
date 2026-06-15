from board_dao import *

board_dao = BoardDAO()


#커넥션 테스트
# board_dao.get_connection()

while True:
    try:
        print("=" * 40)
        print("1.목록  2.등록  3.내용  0.종료")
        print("=" * 40)

        menu = int(input("선택 > "))

        if menu not in range(4):
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        if menu == 0:
            break
        elif menu == 1:# 게시판 select * from board
            boards = board_dao.select_all()
            # print(boards)
            
            print()
            for board in boards:
                print(board[0],
                    board[1],
                    board[2],
                    board[3],
                    board[4],
                    board[5])
        
        elif menu == 2:
            
            title = input("제목 > ")
            content = input("내용 > ")
            writer = input("작성자 > ")

            board_dao.register(title,content,writer)

        elif menu == 3:
            while True:
                try:
                    input_id = int(input("게시판 번호를 입력하세요.(취소:0) > "))

                    board = board_dao.select_one(input_id)
        
                    if input_id == 0:
                        print("실행 취소.")
                        break
                    if not board:
                        print("존재하지 않는 게시판입니다.")
                        continue
                    print()
                    print("번호 :", board[0])
                    print("제목 :", board[1])
                    print("내용 :", board[2])
                    print("작성자 :", board[3])
                    print("작성일 :", board[4])
                    print("수정일 :",board[5])

                    print("=" * 40)
                    print("1.수정  2.삭제  3.댓글  0. 뒤로가기")
                    print("=" * 40)
                    while True:
                        try:
                            menu2 = int(input("선택 > "))

                            if menu2 not in range(4):
                                print("잘못된 입력입니다. 다시 입력하세요.")
                                continue

                            if menu2 == 0:
                                print("뒤로가기")
                                break

                            elif menu2 == 1:
                                edit_title = input("수정할 제목을 입력하세요 > ")
                                edit_content = input("수정할 내용을 입력하세요 > ")

                                board = board_dao.update(edit_title,edit_content,input_id)

                            elif menu2 == 2:
                                while True:
                                    real_del = input("정말 삭제하시겠습니까?\ny / n > ")
                                    if real_del not in ["y","n"]:
                                        print("다시 입력해주세요.")
                                        continue
                                    
                                    if real_del == "y":
                                        board_dao.delete(input_id)
                                        board_dao.delete_all_comment(input_id)
                                        

                                    elif real_del == "n":
                                        print("삭제 취소.")
                                    
                                    break

                            elif menu2 == 3:
                                comments = board_dao.comment_all(input_id)
                                if comments:
                                    print()
                                    print("=" * 40)
                                    for comment in comments:
                                        print(comment[1],
                                              comment[2])
                                else:
                                    print("댓글이 없습니다.")
                                
                                print("=" * 40)
                                print("1.추가  2.수정  3.삭제  0. 뒤로가기")
                                print("=" * 40)
                                
                                while True:
                                    try:
                                        menu3 = int(input("선택 > "))
                                        if menu3 not in range(4):
                                            print("잘못된 입력입니다. 다시 입력하세요.")
                                            continue

                                        if menu3 == 0:
                                            print("뒤로가기")
                                            break

                                        elif menu3 == 1:
                                            input_content = input("추가할 내용을 입력하세요 > ")
                                            board_dao.add_comment(input_id, input_content)

                                        elif menu3 == 2:
                                            while True:
                                                    try:
                                                        edit_no = int(input("수정할 댓글 번호를 입력하세요(취소:0) > "))

                                                        if edit_no == 0:
                                                            break

                                                        content = board_dao.comment_one(input_id,edit_no)

                                                        if not content:
                                                            print("댓글이 존재하지 않습니다. 다시 입력해주세요.")
                                                            continue
                                                        
                                                        else:
                                                            edit_content = input("수정할 내용을 입력하세요 > ")
                                                            board_dao.edit_comment(edit_content,input_id, edit_no)
                                                            break
                                                    except ValueError:
                                                        print("숫자가 아닙니다.")
                                                        continue

                                        elif menu3 == 3:
                                            while True:
                                                    try:
                                                        delete_no = int(input("삭제할 댓글 번호를 입력하세요(취소:0) > "))

                                                        if delete_no == 0:
                                                            break

                                                        content = board_dao.comment_one(input_id,delete_no)

                                                        if not content:
                                                            print("댓글이 존재하지 않습니다. 다시 입력해주세요.")
                                                            continue

                                                        else:
                                                            board_dao.delete_comment(input_id, delete_no)
                                                            break
                                                    except ValueError:
                                                        print("숫자가 아닙니다.")
                                                        continue
                                                    
                                    except ValueError:
                                        print("숫자가 아닙니다.")
                                        continue
                                    break
                            break

                        except ValueError:
                            print("숫자를 입력해 주세요.")
                            continue

                except ValueError:
                    print("숫자가 아닙니다.")
                    continue  

                break

    except ValueError:
        print("숫자를 입력해 주세요.")
        continue

            




print("게시판 종료")