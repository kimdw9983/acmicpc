# acmicpc
- 지원언어: Python, PyPy
- PS용 예제 입력 자동화 및 유닛 테스트 기능 구현
- 테스트 케이스별로 자동 채점
- 다양한 PS 템플릿 배포

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=kimdw9983)](https://solved.ac/kimdw9983)
- 코드 템플릿 중 다수는 [Pyrival](https://github.com/cheran-senthil/PyRival)을 참고합니다.

## 목표
- 어떤 경우에서도 소스파일의 내용물을 그대로 복사 붙여넣기 한 것이 제출 가능한 코드여야 합니다.
  - 제출을 하기 위해 코드 변환 스크립트를 실행하거나 하는등의 과정이 일절 필요 없습니다.\
  디버그 함수들만 지우면 됩니다.
- zero dependancy. 내장 모듈을 제외한 어떤 의존성도 없습니다. 
  - offline 환경에서도 작동하는 것을 목표로 합니다.
  - psutil은 제거예정 입니다.
- 유연성. 테스트 케이스를 추가하거나 제거하는 것을 최대한 간편해야 합니다.
- 편의성. PS를 하면서 쓸만한 유용한 디버그 함수들을 사용할 수 있습니다.

## 사용법
- VSCode 환경에서만 작동합니다.
- Python과 PyPy가 환경 변수에 등록되어 있어야 합니다.
- `testcases/input.acmicpc` 에 원하는 입력을 넣습니다. 
  - 각 테스트케이스의 구분은 `;;` 혹은 `//` 입니다.
- tests 폴더에 문제를 푸는 `*.py` 파일을 넣고 실행(F5)합니다.