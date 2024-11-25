"use client";

import { useState, useEffect, useRef } from "react";
import { createClient } from "@/lib/client";
import Link from "next/link";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import "dayjs/locale/en"; // Load English locale
import InsertLikes from "@/components/insertLikes";

// إعداد Day.js لتنسيقات الوقت
dayjs.extend(relativeTime);

// تعريف واجهة Palette
interface Palette {
  id: string;
  color1: string;
  color2: string;
  color3: string;
  color4: string;
  created_at: string;
  likes_count: number;
}

// Hook لجلب البيانات
function usePalettes(
  limit: number = 20,
  from: "random_colors_view" | "colors" = "colors"
) {
  const [palettes, setPalettes] = useState<Palette[]>([]);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const fetchPalettes = async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    const supabase = createClient();

    try {
      const { data, error } = await supabase
        .from(from)
        .select("*,likes_count (id,likes_count)")
        .range(offset, offset + limit - 1);

      if (error) {
        console.error("Error fetching palettes:", error);
        return;
      }

      if (data) {
        setPalettes((prev) => [...prev, ...data]);
        setOffset((prevOffset) => prevOffset + limit);
        if (data.length < limit) setHasMore(false);
      }
    } catch (error) {
      console.error("Unexpected error:", error);
    } finally {
      setLoading(false);
    }
  };

  return { palettes, loading, hasMore, fetchPalettes };
}

// مكون عرض الألوان
export default function View() {
  const { palettes, loading, hasMore, fetchPalettes } = usePalettes(20, "colors");
  const observerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && hasMore && !loading) {
          fetchPalettes();
        }
      },
      { rootMargin: "200px" }
    );

    if (observerRef.current) observer.observe(observerRef.current);

    return () => observer.disconnect();
  }, [fetchPalettes, hasMore, loading]);

  return (
    <div className="w-full h-full">
      <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
        {palettes.map(
          ({ id, color1, color2, color3, color4, created_at, likes_count }) => (
            <div key={id} className="flex flex-col justify-center items-center">
              <Link
                href={`/palette/${id}`}
                className="w-full h-20 rounded-t-xl"
                style={{ backgroundColor: `#${color1}` }}
              ></Link>
              <Link
                href={`/palette/${id}`}
                className="w-full h-14"
                style={{ backgroundColor: `#${color2}` }}
              ></Link>
              <Link
                href={`/palette/${id}`}
                className="w-full h-10"
                style={{ backgroundColor: `#${color3}` }}
              ></Link>
              <Link
                href={`/palette/${id}`}
                className="w-full h-10 rounded-b-xl"
                style={{ backgroundColor: `#${color4}` }}
              ></Link>
              <div className="w-full flex justify-between items-center py-3">
                <InsertLikes
                  likes_count={
                    Array.isArray(likes_count)
                      ? likes_count.length
                      : likes_count
                  }
                  id={color1 + color2 + color3 + color4}
                  color1={color1}
                  color2={color2}
                  color3={color3}
                  color4={color4}
                />
                <h4 className="text-xs font-normal opacity-80">
                  {dayjs(created_at).locale("ar").fromNow()}
                </h4>
              </div>
            </div>
          )
        )}
      </div>
      <div ref={observerRef}></div>
      {loading && (
        <p className="text-sm text-gray-500">Loading more palettes...</p>
      )}
      {!hasMore && (
        <p className="text-sm text-gray-500">No more palettes to display.</p>
      )}
    </div>
  );
}
