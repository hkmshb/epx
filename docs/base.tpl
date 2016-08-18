<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>ePinXtractr {{ title }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="generator" content="{{ app.name }} v{{ app.version }}">
    <style type="text/css">
/*! normalize.css v3.0.2 | MIT License | git.io/normalize */ img,legend{border:0}legend,td,th{padding:0}html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,optgroup,strong{font-weight:700}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre,textarea{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}table{border-collapse:collapse;border-spacing:0}
/* Skeleton V2.0.4 | Copyright 2014, Dave Gamache */ .column,.columns,.container,.u-full-width{width:100%;box-sizing:border-box}h1,h2,h3{letter-spacing:-.1rem}body,h6{line-height:1.6}.container{position:relative;max-width:960px;margin:0 auto;padding:0 20px}ol,p,ul{margin-top:0}.column,.columns{float:left}@media (min-width:400px){.container{width:85%;padding:0}}html{font-size:62.5%}body{font-size:1.5em;font-weight:400;font-family:Raleway,HelveticaNeue,"Helvetica Neue",Helvetica,Arial,sans-serif;color:#222}h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:2rem;font-weight:300}h1{font-size:4rem;line-height:1.2}h2{font-size:3.6rem;line-height:1.25}h3{font-size:3rem;line-height:1.3}h4{font-size:2.4rem;line-height:1.35;letter-spacing:-.08rem}h5{font-size:1.8rem;line-height:1.5;letter-spacing:-.05rem}h6{font-size:1.5rem;letter-spacing:0}@media (min-width:550px){.container{width:80%}.column,.columns{margin-left:4%}.column:first-child,.columns:first-child{margin-left:0}.one.column,.one.columns{width:4.66666666667%}.two.columns{width:13.3333333333%}.three.columns{width:22%}.four.columns{width:30.6666666667%}.five.columns{width:39.3333333333%}.six.columns{width:48%}.seven.columns{width:56.6666666667%}.eight.columns{width:65.3333333333%}.nine.columns{width:74%}.ten.columns{width:82.6666666667%}.eleven.columns{width:91.3333333333%}.twelve.columns{width:100%;margin-left:0}.one-third.column{width:30.6666666667%}.two-thirds.column{width:65.3333333333%}.one-half.column{width:48%}.offset-by-one.column,.offset-by-one.columns{margin-left:8.66666666667%}.offset-by-two.column,.offset-by-two.columns{margin-left:17.3333333333%}.offset-by-three.column,.offset-by-three.columns{margin-left:26%}.offset-by-four.column,.offset-by-four.columns{margin-left:34.6666666667%}.offset-by-five.column,.offset-by-five.columns{margin-left:43.3333333333%}.offset-by-six.column,.offset-by-six.columns{margin-left:52%}.offset-by-seven.column,.offset-by-seven.columns{margin-left:60.6666666667%}.offset-by-eight.column,.offset-by-eight.columns{margin-left:69.3333333333%}.offset-by-nine.column,.offset-by-nine.columns{margin-left:78%}.offset-by-ten.column,.offset-by-ten.columns{margin-left:86.6666666667%}.offset-by-eleven.column,.offset-by-eleven.columns{margin-left:95.3333333333%}.offset-by-one-third.column,.offset-by-one-third.columns{margin-left:34.6666666667%}.offset-by-two-thirds.column,.offset-by-two-thirds.columns{margin-left:69.3333333333%}.offset-by-one-half.column,.offset-by-one-half.columns{margin-left:52%}h1{font-size:5rem}h2{font-size:4.2rem}h3{font-size:3.6rem}h4{font-size:3rem}h5{font-size:2.4rem}h6{font-size:1.5rem}}a{color:#1EAEDB}a:hover{color:#0FA0CE}.button,button,input[type=submit],input[type=reset],input[type=button]{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:11px;font-weight:600;line-height:38px;letter-spacing:.1rem;text-transform:uppercase;text-decoration:none;white-space:nowrap;background-color:transparent;border-radius:4px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}.button:focus,.button:hover,button:focus,button:hover,input[type=submit]:focus,input[type=submit]:hover,input[type=reset]:focus,input[type=reset]:hover,input[type=button]:focus,input[type=button]:hover{color:#333;border-color:#888;outline:0}.button.button-primary,button.button-primary,input[type=submit].button-primary,input[type=reset].button-primary,input[type=button].button-primary{color:#FFF;background-color:#33C3F0;border-color:#33C3F0}.button.button-primary:focus,.button.button-primary:hover,button.button-primary:focus,button.button-primary:hover,input[type=submit].button-primary:focus,input[type=submit].button-primary:hover,input[type=reset].button-primary:focus,input[type=reset].button-primary:hover,input[type=button].button-primary:focus,input[type=button].button-primary:hover{color:#FFF;background-color:#1EAEDB;border-color:#1EAEDB}input[type=tel],input[type=url],input[type=password],input[type=email],input[type=number],input[type=search],input[type=text],select,textarea{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #D1D1D1;border-radius:4px;box-shadow:none;box-sizing:border-box}input[type=tel],input[type=url],input[type=password],input[type=email],input[type=number],input[type=search],input[type=text],textarea{-webkit-appearance:none;-moz-appearance:none;appearance:none}textarea{min-height:65px;padding-top:6px;padding-bottom:6px}input[type=tel]:focus,input[type=url]:focus,input[type=password]:focus,input[type=email]:focus,input[type=number]:focus,input[type=search]:focus,input[type=text]:focus,select:focus,textarea:focus{border:1px solid #33C3F0;outline:0}label,legend{display:block;margin-bottom:.5rem;font-weight:600}fieldset{padding:0;border-width:0}input[type=checkbox],input[type=radio]{display:inline}label>.label-body{display:inline-block;margin-left:.5rem;font-weight:400}ul{list-style:circle inside}ol{list-style:decimal inside}ol,ul{padding-left:0}ol ol,ol ul,ul ol,ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}.button,button,li{margin-bottom:1rem}code{padding:.2rem .5rem;margin:0 .2rem;font-size:90%;white-space:nowrap;background:#F1F1F1;border:1px solid #E1E1E1;border-radius:4px}pre>code{display:block;padding:1rem 1.5rem;white-space:pre}td,th{padding:12px 15px;text-align:left;border-bottom:1px solid #E1E1E1}td:first-child,th:first-child{padding-left:0}td:last-child,th:last-child{padding-right:0}fieldset,input,select,textarea{margin-bottom:1.5rem}blockquote,dl,figure,form,ol,p,pre,table,ul{margin-bottom:2.5rem}.u-max-full-width{max-width:100%;box-sizing:border-box}.u-pull-right{float:right}.u-pull-left{float:left}hr{margin-top:3rem;margin-bottom:3.5rem;border-width:0;border-top:1px solid #E1E1E1}.container:after,.row:after,.u-cf{content:"";display:table;clear:both}
/* ePinXtractr v1.0 */ @font-face{font-family:Roboto;src:url(fonts/Roboto-Regular.ttf) format('truetype')}html{position:relative;min-height:100%}h1{font-size:40px}h2{font-size:28px}h1,h2{margin:0;padding:0}div{border:0 solid #00f}body{margin:0 0 20px;padding:0;overflow-y:scroll;background-color:#fff;font:14px/20px Roboto,OpenSans,Verdana,sans-serif;min-width:400px}header{padding:10px 0;border-bottom:solid 2px #ddd}header h1{float:left}header .card{float:right;width:300px}header .card .info{float:right;text-align:right;padding-right:10px}header .card img{float:right;width:70px;height:55px}footer{border-top:solid 1px #ddd;padding:6px 0;background-color:#f3f3f3;color:#777;font-size:12px;z-index:1015;position:absolute;left:0;right:0;bottom:0;width:100%;height:20px}.page{padding-top:20px}section{padding:5px 0 15px}section h2{padding-bottom:5px;margin-bottom:10px;border-bottom:solid 1px #ddd}section li{list-style-position:outside;margin-left:10px}table{margin:10px 20px}table td{padding:5px}table caption{text-align:left;font-weight:700}ol ol,ol ul,ul ol,ul ul{font-size:100%}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{{ title }}</h1>
            <div class="card">
                <img src="{{ app.logo_path }}"/>
                <div class="info">
                    <h2 class="title">{{ app.name }}</h2>
                    <span class="ver">{{ app.version }}</span>
                </div>
            </div>
        </div>
    </header>
    <div class="page">
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </div>
    <footer>
        <div class="container">
            {{ app.name }} developed with <3 by <a href="http://hazeltek.com">Hazeltek Solutions</a>
        </div>
    </footer>
</body>
</html>