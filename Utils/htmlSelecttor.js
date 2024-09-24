// isValid()
// - 이 함수는 주어진 문자열이 null, undefined, 또는 공백만으로 이루어져 있지 않은지를 확인합니다.
function isValid(str) {
    return str !== null && str !== undefined && str.trim() !== '';
}

// trimEndSep()
// - 문자열의 끝에 포함된 특정 구분자를 제거
// endsWith(separator): 문자열이 지정된 구분자로 끝나는지 확인합니다.
// slice(0, -separator.length): 구분자가 발견되면, slice() 메서드를 사용해 문자열의 끝에서 구분자의 길이만큼 제거한 새로운 문자열을 반환합니다.
// -separator.length는 문자열의 끝에서부터 구분자의 길이만큼의 부분 문자열을 제거하는 것을 의미합니다.
// 구분자가 없으면 원본 문자열을 반환: 문자열이 구분자로 끝나지 않으면 원본 문자열을 그대로 반환합니다.
function trimEndSep(str, separator) {
    if (str.endsWith(separator)) {
        return str.slice(0, -separator.length); // 구분자를 제거한 새로운 문자열 반환
    }
    return str; // 구분자가 없으면 원본 문자열 반환
}

// 사용 예시
console.log(trimEndSep("apple,orange,banana,", ",")); // "apple,orange,banana"
console.log(trimEndSep("apple,orange,banana", ","));  // "apple,orange,banana"
console.log(trimEndSep("apple orange banana", ","));   // "apple orange banana"


// TFS - Grid| 특정 키워드의 Elements를 선택 (InnerHTML)
function selectInnerHTML(elSelector, child_keywords) {
    // querySelectorAll을 사용하여 클래스가 일치하는 모든 요소를 선택
    const elements = document.querySelectorAll(elSelector);
    const selection = window.getSelection();

    // 기존 선택된 내용 제거
    selection.removeAllRanges();

    // 각 요소에 대해 범위를 설정하고 선택
    elements.forEach((element) => {
      const range = document.createRange();
      range.selectNodeContents(element);
      selection.addRange(range);

      // 각 요소의 innerHTML를 콘솔에 출력
      // console.log(element.innerHTML);

      if(element.childElementCount > 0) {
        let nodeValue = '';

        element.childNodes.forEach((node, child_idx) => {
            switch (child_idx) {
                case 0:
                    nodeValue += `Commit: ${node.textContent}`;
                    break;
                case 1:
                    nodeValue += `Author: ${node.textContent}`;
                    if (isValid(child_keywords) && node.textContent.includes(child_keywords)) {
                        // 선택 요소 색 변경 & 글씨체 굵게
                        node.style.backgroundColor = 'yellow'; 
                        node.style.fontWeight = 'bold';
                    }
                    break;
                case 2:
                    nodeValue += `Date: ${node.textContent}`;
                    break;
                default:
                    break;
            }
            nodeValue += ' | ';
        });

        console.log(trimEndSep(nodeValue,' | '));

      }
    });
  }

// TFS - Grid| 특정 키워드의 Elements를 선택 (InnerText)
function selectText(elSelector, keyword) {
// 특정 문자를 포함하고 있는지 확인할 키워드
// const keyword = 'special keyword';

// querySelectorAll을 사용하여 클래스가 일치하는 모든 요소를 선택
// const elements = document.querySelectorAll('.text-ellipsis.font-weight-semibold.flex-grow'); // TFS 일반 : '.text-ellipsis.font-weight-semibold.flex-grow'
// const elements = document.querySelectorAll('.commit-title..text-ellipsis.font-weight-semibold.flex-grow'); // TFS 깃 커밋 : '.commit-title.text-ellipsis.font-weight-semibold.flex-grow'
const elements = document.querySelectorAll(elSelector);
const selection = window.getSelection();


// 클래스에 해당하는 요소들의 개수를 콘솔에 출력

console.log(`클래스를 가진 요소의 개수: ${elements.length}`);
console.log('-'.repeat(100));

// 기존 선택된 내용 제거
selection.removeAllRanges();

// 각 요소에 대해 범위를 설정하고 텍스트가 특정 문자를 포함하는 경우에만 콘솔 출력
elements.forEach((element, idx) => {
    const range = document.createRange();
    const text = element.innerText;

    // 특정 문자를 포함하는지 확인
    if (text.includes(keyword)) {
        
    // 텍스트 범위 선택
    range.selectNodeContents(element);
    selection.addRange(range);
    
    // 선택 요소 색 변경 & 글씨체 굵게
    element.style.backgroundColor = 'yellow'; 
    element.style.fontWeight = 'bold';

    // 특정 문자를 포함하는 경우에만 콘솔에 출력
    console.log(`${idx}: ${text}`);
    //console.log(`${idx}: ${element.innerHTML}`);
    }
});
}

seletor = '.text-ellipsis.font-weight-semibold.flex-grow' 
keyword = '[찾을 번호 또는 문구]'
selectText(seletor, keyword);