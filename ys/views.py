from django.http import HttpResponse


def ys_summary(request):
    """Return a summary of the YS method."""
    summary = (
        "YS法は、目標達成のための全体的な流れを8段階に分け、"
        "計画から実行、改善までを体系的に進める手法です。具体的には、次のポイントが特徴です。\n\n"
        "- 明確な目標設定と現状把握：テーマや背景を整理し、具体的な数値目標を定め、"
        "現状とのギャップを可視化します。\n"
        "- Goal Magic Wandによる対策の枝分かれ図：段階的に対策を展開し、重要度と達成可能性を"
        "評価して枝分かれ図で視覚化します。\n"
        "- Concentration Chart（グラウ）での対策絞り込み：重要度×達成可能性で対策を分類し、"
        "優先すべき行動を明確化します。\n"
        "- スケジュール化と実行・改善：行動計画をスケジュールに落とし込み、実績と目標の差を"
        "分析しながら継続的に改善します。\n\n"
        "こうした手順を踏むことで、限られた資源の中でも効果的な行動を選択しやすくなり、"
        "目標達成の確度を高めることができます。"
    )
    return HttpResponse(summary, content_type="text/plain; charset=utf-8")
