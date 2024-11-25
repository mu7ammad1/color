"use client";

import { usePopular } from "@/hooks/usePalettes";
import Link from "next/link";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import "dayjs/locale/en"; // Load English locale
import InsertLikes from "@/components/insertLikes";
import { useEffect, useRef } from "react";

dayjs.extend(relativeTime);

export default function Popular_components() {
  const { palettes, loading, hasMore, fetchPalettes } = usePopular(20);
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
