import { defineUserConfig } from 'vuepress'
import { defaultTheme } from 'vuepress'

import { backToTopPlugin } from '@vuepress/plugin-back-to-top'
import { pwaPlugin } from '@vuepress/plugin-pwa'
import { pwaPopupPlugin } from '@vuepress/plugin-pwa-popup'
import { googleAnalyticsPlugin } from '@vuepress/plugin-google-analytics'
import { searchPlugin } from '@vuepress/plugin-search'

import { tasklist } from "@mdit/plugin-tasklist";

import type { DefaultThemeOptions } from 'vuepress'


export default defineUserConfig({
    // 站点配置
    lang: 'zh-CN',
    title: '题库',
    description: 'Ciallo～(∠・ω< )⌒☆',
    base: '/',
    head: [
        ['link', { rel: 'icon', href: '/images/www/宁宁.jpg' }]
    ],

    // 给markdown添加解析复选框配置
    extendsMarkdown: (md) => {
        md.use(tasklist, {
          });
    },

    // 插件配置
    plugins: [
        backToTopPlugin(),

        pwaPlugin({
            skipWaiting: true
        }),

        pwaPopupPlugin({
            locales: {
                '/': {
                    message: '发现新内容可用',
                    buttonText: '刷新',
                }
            }
        }),

        googleAnalyticsPlugin({
            id: 'G-DC97NQD68V'
        }),

        searchPlugin()
    ],

    // 主题和它的配置
    theme: defaultTheme({
        repo: 'Redmomn/USTH_question_bank',
        docsRepo: 'Redmomn/USTH_question_bank',
        docsBranch: 'master',
        docsDir: 'docs',
        editLinkText: "编辑此页",
        lastUpdated: true,
        lastUpdatedText: '上一次编辑',
        contributors: true,
        contributorsText: '贡献者',
        tip: "提示",
        warning: "注意",
        danger: "警告",
        backToHome: "返回首页",
        navbar: [
            { text: '开始', link: '/guide/' },
            {
                text: '题库', children: [
                    { text: '马原', link: '/tiku/1001马克思主义基本原理概论/马克思主义基本原理概论.md' },
                    { text: '毛概', link: '/tiku/1003毛概/毛概.md' },
                    { text: '新思想（2023）', link: '/tiku/1033新思想概论（2023年）/新思想概论（2023年）.md' },
                    { text: '近代史', link: '/tiku/1005中国近现代史纲要/中国近现代史纲要.md' }
                ]
            },
            { text: '常见问题', link: '/question/' }
        ],
        sidebar: "auto",
    }),

})
