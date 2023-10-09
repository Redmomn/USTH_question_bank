import { defineUserConfig } from 'vuepress'
import type { DefaultThemeOptions } from 'vuepress'

export default defineUserConfig<DefaultThemeOptions>({
    // 站点配置
    lang: 'zh-CN',
    title: '题库',
    description: 'Ciallo～(∠・ω< )⌒☆',
    base: '/',
    head: [
        ['link', { rel: 'icon', href: '/images/www/宁宁.jpg' }]
    ],
    plugins: [
        ['@vuepress/back-to-top'],
        [
            '@vuepress/pwa',
            {
                skipWaiting: true
            }
        ],
        [
            '@vuepress/plugin-pwa-popup',
            {
                locales: {
                    '/': {
                        message: '发现新内容可用',
                        buttonText: '刷新',
                    }
                }
            }
        ],
        [
            '@vuepress/plugin-google-analytics',
            {
                id: 'G-DC97NQD68V'
            }
        ],
        [
            "@vuepress/plugin-docsearch",
            {

            }
        ]
    ],

    // 主题和它的配置
    theme: '@vuepress/theme-default',
    themeConfig: {
        repo: 'Redmomn/USTH_question_bank',
        docsRepo: 'Redmomn/USTH_question_bank',
        docsBranch: 'master',
        docsDir: 'docs',
        editLinkText: "编辑此页",
        lastUpdated: true,
        lastUpdatedText: '上一次编辑',
        contributors: true,
        tip: "提示",
        warning: "注意",
        danger: "警告",
        backToHome: "返回首页",
        navbar: [
            { text: '开始', link: '/guide/' },
            {
                text: '题库', children: [
                    { text: '马原', link: '/1001马克思主义基本原理概论/马克思主义基本原理概论.md' },
                    { text: '毛概', link: '/1003毛概/毛概.md' },
                    { text: '新思想（2023）', link: '/1033新思想概论（2023年）/新思想概论（2023年）.md' }
                ]
            },
            {text: '常见问题', link: '/question/'}
        ],
        sidebar: "auto",
    },

})
