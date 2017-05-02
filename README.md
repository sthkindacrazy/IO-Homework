# IO-Homework
IO-Homework

## 작성한 파일들에 대한 간단한 설명

- utils.py
>+ HTTP request, API calling을 담당

- blockexplorer.py
>+ Block정보와 관련된 여러가지 클래스 정의
>+ Block정보 가져오기
>+ utils.py와 blockexplorer.py는 제공된 blockchain API (python)을 참고함

- blockdata.py
>+ 1,2번 문제들을 해결하기 위한 function들 정의

- test_blockdata.py
>+ blockdata.py에 대한 test function

- etc_test.py
>+ blockdata.py의 function들에 대한 직접적 테스트는 아니지만 문제를 풀면서 필요한 간단한 unit test 포함
>+ test_blockdata.py를 작동 시키기 위한 전처리 코드들도 일부 포함

## 실행
모든 프로그램 .py 파일을 다운 받은 후
커맨드라인에서 다음과 같이 실행


- 1번
```bash
$ python3 -i blockdata.py
>>> print_tx_parameters("block_hash")
```

- 2번
```bash
$ python3 -i blockdata.py
>>> in_out_valPrint(hash_order)
```

- TEST
```bash
$ python3 -i test_blockdata.py
```

내부 함수화 라이브러리화 해서 사용할 가능성이 더 많은 기능들이라 생각해서 커맨드창에서 input을 받지는 않았음. 

## 1번 문제에 대한 접근

- Number of Transactions
>+ 첫번째 고민은 'block.n_tx'와 'len(block.transactions)'의 길이가 같은지
>+ 이러한 고민을 했던 이유는 'unconfirmed transactions'들의 존재 때문임
>+ 둘 중에 어느 하나는 'unconfirmed'가 포함되고 어느 하나는 포함하지 않는다면 문제.
>+ 'block.transactions[i].block_height == -1' 이면 'unconfirmed transactions'이기 때문에 개수를 하나씩 세면서 체크 -> enc_test.py에서 구현.
>+ 'block.n_tx' == 'len(block.transactions)' 이며 'unconfirmed transactions'는 포함이 된 것이 아님.
>+ 'block.n_tx' 를 return 하는 function 구현

- Average Value of Transactions
>+ 각 transactions에서 출력(out)의 value를 모두 더한 후 'block.n_tx'로 나눠준 값
>+ 단위는 BTC로 모두 통일하기 위해서 10^8으로 나눠 자릿수를 맞춰줌

- Average Fee of Transactions
>+ 해당 블록의 fee를 트랜잭션의 개수로 나눈 값.
>+ 마찬가지로 단위는 BTC로 통일 시켜줌

- Average Size of Transactions 
>+ 각 트랜잭션의 size를 루프를 돌며 'block.n_tx'로 나눠준 값을 구함
>+ API struct에서 정의한 int 형식 그대로 받아서 사용하나 결과 return에서 나눠주기 때문에 소숫값이 나옴.


### 1번 문제에 대한 기타 고민

- function들이 전부 block hash를 받을 것인가 아니면 block 혹은 다른 필요 파라미터들만 받을 것인가.
- 처음에는 tot_tx, avg_tx_val 같은 function들이 모두 block_hash 값 그 자체를 받았다. 처음 생각으로는 이렇게 코딩하는 것이 각각 함수들을 불러쓸 때, 그러니까 평균, 총합 등을 따로 불러쓸 때 편할 것이라 생각했으나 get_block이 시간을 꽤 잡아먹었다. (싸지방이라서 그런가인지는 모르겠다.)
- 되도록이면 get_block은 한번만 콜하고 대신 그렇게 불러낸 block 하나를 변수로 각각에 넣어주기로 했다. 필요한 변수들, 예를 들면 avg_tx_val에 block.n_tx와 tx 정보만을 넘겨주는 형식으로 변수를 세분화 하면 통일성을 갖고 쉽게 불러쓰는 모듈과는 조금 거리가 멀어진다 생각했다.  block구조안에서 fee, n_tx를 바로 부를 수 있는데 input parameter를 늘릴 필요가 없다고 생각했다.
- 그래서 최종적으로는 print_tx_parameters(block_hash) function 안에서 block_hash로 block 정보를 한번만 구성하고 나머지 sub_function들을 콜하는 형태로 구성했다. 

### 1번 문제에 대한 TEST
- test_blockdata.py에서 구현했다. 나눗셈의 경우 차의 절댓값이 0.00...1 차이 이내면 같은 것으로 보았다.
- test case 선정에 있어서 마지막 transaction, 거의 첫 transaction, 중간 transaction 등을 포함한 다양한 block_hash로 골랐다.


## 2번 문제에 대한 접근

- 일단 처음 봤을 때 든 생각은 block_hash - 명령어 조합을 어떻게 parse할 것인가.
- [hash_value] input 형태이기 때문에 [hash_value]와 input/output은 Python의 split을 사용하자
- hash는 숫자와 알파벳의 조합이므로 [hash_value]에서 hash_value만을 뽑아내는것은 정규표현식을 사용하자.

### 2번 문제에 대한 기타 고민
- 처음에는 input과 output 출력을 모두 하나의 function, in_out_valPrint(hash_order)안에다 넣었다.
- input값과 output 출력은 후에도 각각 활용가능성이 높다고 생각, 따로 input_print, output_print로 만들었다.
- 이 때 각각의 값들을 받아줄 때 list를 사용하는데, set은 indexing이 되지 않으며 tuple도 list에 비해 불편하다. 후에 DB 같은 것에 넣는 작업을 한다면 list로 받아주는게 나을 것이라 가정했다. 

### 2번 문제에 대한 TEST
- enc_test.py에서 unit test처럼 정규표현식 즉 hash-명령어 조합이 잘 되는지 parsing test를 하고 출력값에 대한 테스트는 실제 홈페이지에서 출력된 값들과 같은지 확인하는것으로 했다. 


## Epilogue
 - TEST code를 Formalize(?) 하는 것이 까다로웠다.
 - 어떤 식으로 정형화된 테스트 코드를 쓰는 것이 좋을지 고민을 많이 할 수 있었다. 
 - 제대로 된 IDE 없이 코딩을 해서 잔실수로 인해 commit을 좀 남발한 것처럼 보이게 된 것이 후회스럽다.
 - 여러가지 조건 또 block chain에 대한 이해, 그리고 function이 중간에 제대로 된 값을 출력하는지 보기 위해 unit test는 많이 했는데 script 형태로 대부분 작성하고 test-code라고 불릴만한 형태로 정리하지 못했는데 어느 범주까지가 formalized test-code/function에 포함되어야 하는지 고민이다. 

- 생각을 하면 할수록 더 고민되는 부분이 많긴 했지만 덕분에 재미있는 시간이 된 것 같습니다. 감사합니다.
