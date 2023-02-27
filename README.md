<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>[Python] AUTO_UPBIT</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-opaquegray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="8f23dd85-9eeb-4154-804e-2945bb21cf34" class="page sans"><header><h1 class="page-title">[Python] AUTO_UPBIT</h1></header><div class="page-body"><p id="e9db425c-e548-476c-aef3-0e2eb7a9200e" class="">
</p><figure id="2cff5c05-d7a8-4fad-8895-52a02902225c"><div class="source">https://github.com/GoToGREAT/AutoCrypto</div></figure><p id="81f4a69d-cec9-494e-b652-0f27a49012d9" class="">
</p><p id="7c5711ef-0cd4-4d04-b0af-e785c81cf1ff" class="">
</p><h3 id="d7cb8e37-ffe1-4c66-8f16-544ee93e6670" class="">개발 목표 : 파이썬을 통한 업비트 코인 자동 매매</h3><h3 id="ea0f6e09-1213-4b15-96d7-7e3bde784a55" class="">프로그램 개발기간 : 10.31-</h3><p id="34dbc56f-d278-4ac9-92ef-56ccb1d0d3c8" class=""> - 개인적 사용을 위한 프로젝트 수정 보완은 계속 될 예정입니다.</p><h3 id="3926de53-19af-4c4c-90d2-de52bdc72a46" class="">수행인원 : 1인 프로젝트</h3><h3 id="021619e7-698c-492b-b28a-ebfec909acff" class="">사용 언어</h3><p id="2aa8122a-bc62-449b-80da-ee029900141b" class=""><strong>프로그램</strong></p><p id="e3db640c-0f66-4dc9-b902-49e418cf3d84" class=""><strong> - BACKEND : Python 3.8.9, Visual Studio Code</strong></p><p id="b2243a68-eaa9-4d17-9dd1-2b0b0fa8b36c" class="">
</p><p id="8b58206c-10b8-48df-a12d-e3ae247c7106" class=""><strong>서버 구축(예정) : AWS + UBUNTU</strong></p><p id="ecad3935-b4bc-4160-b42a-911f905944f0" class="">
</p><h3 id="f7b0b5eb-7f58-4fd2-a59b-6cd9eb63c8ee" class="">구현 기능</h3><p id="7f4ed759-eff5-4fb5-bb83-bfd2388abecd" class="">
</p><p id="9e10d0e2-bbaa-4818-bdda-1bb82e1d0ba3" class=""><strong><mark class="highlight-gray_background">BASIC   ——————————————————————————————</mark></strong><div class="indented"><p id="c2bf89e6-267e-4019-89d8-28680e9b50ab" class="">22.10.30 - 22.11.01 제작 완료</p></div></p><ul id="8b991b80-8e55-4b23-aa9f-7397421d4bb9" class="bulleted-list"><li style="list-style-type:disc"><strong>test.py  : pyupbit api를 활용하여 업비트 연결</strong></li></ul><ul id="52eb647e-8aa1-4bfb-b2bf-6858aa89e972" class="bulleted-list"><li style="list-style-type:disc"><strong>bestk : 자동매매 기법을 위한 최대 이익 k를 구하는 코드</strong></li></ul><ul id="e04f687a-e91e-407f-81bc-082cc8f4dd6e" class="bulleted-list"><li style="list-style-type:disc"><strong>backtest.py : 과거 차트를 분석하여 k로 프로그램 설정 시 수익 가능했던 이익 확인</strong><p id="bb2078cc-bf42-4c19-9c84-30510866a1f0" class=""><strong>                      dd.xlsx으로 결과 데이터 저장</strong></p></li></ul><ul id="660e69dc-fd19-47d6-9dd8-e7374edffba1" class="bulleted-list"><li style="list-style-type:disc"><strong>bitcoinAutoTrade.py : 자동 매매 진행 코드</strong></li></ul><ul id="d61b80b5-b754-48dc-a76a-b62da525f7a6" class="bulleted-list"><li style="list-style-type:disc"> 변동성 돌파 전략 : 일봉 데이터를 이용하여 <strong>거래일의 현재가가 (시가 + 전일 변동폭 * 0.5)를 돌파할 때 매수하고 종가에 매도하는 전략</strong></li></ul><p id="9873780e-8b6b-426d-9abe-0490ee9cac95" class="">
</p><p id="847e6f91-634b-4687-b32c-f095f44e0e4e" class=""><strong><mark class="highlight-gray_background"> DOGE ——————————————————————————————</mark></strong><div class="indented"><p id="51f3dd76-832c-4ac2-870b-8fe18607bde0" class="">제작 중 / api 제공 프로그램의 보안 이슈로 private 관리 / 11.08 AWS 서버 구축 및 시세 탐지</p><p id="999c35b2-d091-4ae7-9795-237f2713617d" class="">/ 11.09 AWS 자동매매 시작</p></div></p><ul id="c571944d-d309-4d7f-86d0-4e5152c997e5" class="bulleted-list"><li style="list-style-type:disc"><strong>DogeAutoTrade.py :  60일 이동평균선 이상 매수, 20일 이동평균선 이하 매도</strong></li></ul><ul id="b326e7c1-e482-4481-a0f4-4469f073e623" class="bulleted-list"><li style="list-style-type:disc"><strong>backtest_MovingAverageLine.py : 과거 차트를 분석하여 60일 이동평균선 매매법 실시 시 수익 가능했던 이익 확인</strong></li></ul><ul id="b23932c4-990a-4cab-bc57-3cac32165961" class="bulleted-list"><li style="list-style-type:disc"><strong>slacktest.py : 슬랙 연동하여 챗봇 메세지 전송 가능</strong></li></ul><ul id="2b59662b-6aeb-4e72-ba06-d83d1c0b0895" class="bulleted-list"><li style="list-style-type:disc"><strong>GoldenCross 알고리즘과 Backtest 완료</strong></li></ul><ul id="44fb8ddb-2610-45cd-9557-1533c1c1ff76" class="bulleted-list"><li style="list-style-type:disc"><strong>PyMySql 연동 완료</strong></li></ul><ul id="8a8771d7-b19f-41e8-bc24-4c4332e91fe8" class="bulleted-list"><li style="list-style-type:disc"><strong>AWS SQL 서버 구축 및 WorkBench 연동 완료</strong></li></ul><p id="d1323d07-88cb-4f71-8298-4b5e0d63cc39" class="">
</p><p id="17f26a50-617b-4062-b7a7-f196b239ac7f" class=""><strong><mark class="highlight-gray_background">OPTIMIZE  ——————————————————————————————</mark></strong><div class="indented"><p id="d7ba8c18-9e91-4025-9f14-2ba450e236f4" class="">제작 예정</p></div></p><ul id="0b033e5e-6c32-471b-b996-897ac3fcb4b3" class="bulleted-list"><li style="list-style-type:disc">최적 이익 머신러닝 제작</li></ul><p id="a5c9e1fc-5391-4edd-b73f-c258429c64fd" class="">
</p><h3 id="efe8528d-c3a8-4a52-9a72-4881db004f52" class="">비고</h3><ul id="4471fbe4-28c1-4614-a4b2-502698ef6bfb" class="bulleted-list"><li style="list-style-type:disc"> 파이썬 공부를 위한 <strong>조코딩 ‘파이썬 비트코인 투자 자동화’</strong>의<strong> 클론코딩 + 개인 최적화 프로젝트</strong>입니다.</li></ul><figure id="322fefb6-14a7-44b3-82b6-59c04f7d9325"><div class="source"><a href="https://www.youtube.com/watch?v=WgXOFtDD6XU&amp;list=PLU9-uwewPMe3KKFMiIm41D5Nzx_fx2PUJ">https://www.youtube.com/watch?v=WgXOFtDD6XU&amp;list=PLU9-uwewPMe3KKFMiIm41D5Nzx_fx2PUJ</a></div></figure><p id="ddc1c0de-87ab-473b-ab1a-de77888b11f7" class="">
</p><h3 id="db560d10-b407-4264-8765-b01a430c174d" class="">참조 자료</h3><ul id="94e9997d-752d-486f-953b-00ccdad135ae" class="bulleted-list"><li style="list-style-type:disc"> <strong>조코딩 ‘파이썬 비트코인 투자 자동화’ 동영상</strong></li></ul><p id="7d10e37e-975d-4c1b-8c7e-98ff5c89a013" class="">
</p><ul id="355a34f8-38c4-4e1e-b816-26022f4604af" class="bulleted-list"><li style="list-style-type:disc"> <strong><strong>파이썬을 이용한 비트코인 자동매매 (개정판) / 지은이 : 조대표 외 1명</strong></strong><p id="7051d72c-b88e-4cd4-add5-349d9f914c88" class=""><a href="https://wikidocs.net/book/1665">https://wikidocs.net/book/1665</a></p><p id="780a619e-48fe-4819-849b-f6effbbd2bf3" class=""><a href="https://www.youtube.com/redirect?event=comments&amp;redir_token=QUFFLUhqbVY2bUhrZ0NXVkt1a2pDS0w3TkhyUDZIQjhJUXxBQ3Jtc0tuaEY0X3h6cm9TUEFDZ3FjLWRGTlNNaXVjTWRkdDJNcXp6TUNMWUJqX0hoX3YxZjNNekxKX0pFUlFSaGJ2dWtyeE12aWtSQlV0Y0QySUwzSGtGdXhCZXpzRFYzYzd1N3U4bjZ2WHA3ZDg0YUpTOTFLbw&amp;q=https%3A%2F%2Fgithub.com%2Fsharebook-kr%2Fbook-cryptocurrency&amp;stzid=Ugxp4ms5JELsICxVPCx4AaABAg">https://github.com/sharebook-kr/book-cryptocurrency</a></p><p id="a7604295-01fb-494f-b489-ddede145673a" class="">
</p></li></ul><ul id="cd52fb74-42fb-4838-bfc9-53e45868ea99" class="bulleted-list"><li style="list-style-type:disc"><strong>조코딩 업비트 비트코인 투자 자동화 강의 코드</strong><p id="3e3e1838-bf2e-4c4d-ad29-2839a86e9e84" class=""><a href="https://www.youtube.com/redirect?event=comments&amp;redir_token=QUFFLUhqblpzVlBIWVZSNG55WWpJNlVEa0MxT3pVeXZpQXxBQ3Jtc0ttU0NnMXdUbnoyZmUwVExpcnVoSGpTWEE4c2xiNUZpSkU3ak1OdXE5WHhfYWVabDdRMkk3TW1vd2ZBNGVnRHpLVGVMZWVzeFQ2RzZQZ0NLOWx2NUFsY2FPR3NEZFU4MGZJM21qNUU3Vk5XaGhVQVo1aw&amp;q=https%3A%2F%2Fgithub.com%2Fyoutube-jocoding%2Fpyupbit-autotrade&amp;stzid=Ugxp4ms5JELsICxVPCx4AaABAg">https://github.com/youtube-jocoding/pyupbit-autotrade</a></p><p id="4b623673-b86a-4876-a316-0fddfa7cf90a" class="">
</p></li></ul></div></article></body></html>
